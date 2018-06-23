from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from accounts.models import Investor
from .models import Choice, Question, Portfolio, Investment, EmbeddedTweet
from .forms import PortfolioForm
import pymysql
import pymysql.cursors
import decimal
import time
import datetime
import requests
from django.conf import settings

class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app/results.html'

def portfolio(request, pk):
    user = request.user
    all_portfolios = Portfolio.objects.all()
    portfolio = Portfolio.objects.get(pk=pk)
    all_investments = Investment.objects.filter(portfolio=portfolio)
    aum = 0.0
    for i in all_investments:
        aum += float(i.original_amt)
    aum = round(aum)
    # get latest valuations to embed in the page
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=settings.SPREADS_DB_PASSWD,
                                 db=settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
            spreads_for_pair = dict()
            for pair in pairs:
                #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                sql = "select * from Spreads where coin = %s order by created_at desc limit 1"
                cursor.execute(sql, (pair,))
                spreads = cursor.fetchall()
                spreads_for_pair[pair] = spreads
                #print("for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

            btc_latest_val = float(spreads_for_pair[pairs[0]][0]["bestbid"])
            eth_latest_val = float(spreads_for_pair[pairs[1]][0]["bestbid"])
            xrp_latest_val = float(spreads_for_pair[pairs[2]][0]["bestbid"])
            xlm_latest_val = 0.5
    finally:
        connection.close()
    investment_created = False
    if 'investment_created' in request.session and request.session['investment_created'] == True:
        request.session['investment_created'] = False
        investment_created = True

    just_signed_up = False
    if 'just_signed_up' in request.session and request.session['just_signed_up'] == True:
        request.session['just_signed_up'] = False
        just_signed_up = True

    not_enough_usd = False
    if 'not_enough_usd' in request.session and request.session['not_enough_usd'] == True:
        request.session['not_enough_usd'] = False
        not_enough_usd = True

    tweet_embedded = False
    if 'tweet_embedded' in request.session and request.session['tweet_embedded'] == True:
        request.session['tweet_embedded'] = False
        tweet_embedded = True

    embedded_tweets = EmbeddedTweet.objects.filter(portfolio=portfolio)

    return render(request, 'app/portfolio.html', {'all_portfolios': all_portfolios, \
        'pk': pk,\
        'user': user,\
        'portfolio': portfolio,\
        'all_investments': all_investments,\
        'aum': aum,\
        'user': request.user,\
        'btc_latest_val': btc_latest_val,\
        'eth_latest_val': eth_latest_val,\
        'xrp_latest_val': xrp_latest_val,\
        'xlm_latest_val': xlm_latest_val,\
        'investment_created': investment_created,\
        'just_signed_up': just_signed_up,\
        'not_enough_usd': not_enough_usd,\
        'tweet_embedded': tweet_embedded,\
        'embedded_tweets': embedded_tweets\
        })

def create_investment(request, portfolio_id):
    usd_amt = float(request.GET.get('usd_amt'))
    if usd_amt > request.user.investor.usd_amt:
        request.session["not_enough_usd"] = True
        return redirect("/app/portfolio/" + str(portfolio_id))
    else:
        request.user.investor.usd_amt = float(request.user.investor.usd_amt) - usd_amt
        request.user.investor.save()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    investment = Investment.objects.create(portfolio=portfolio,
                              original_amt=request.GET.get('usd_amt'),
                              btc_amt=request.GET.get('btc_amt'),
                              eth_amt=request.GET.get('eth_amt'),
                              xrp_amt=request.GET.get('xrp_amt'),
                              xlm_amt=request.GET.get('xlm_amt'),
                              owner=request.user,
                              is_active=False)
    request.session['investment_created'] = True

    current_site = get_current_site(request)
    mail_subject = 'New Investment Received for ' + portfolio.portfolio_name
    html_content = render_to_string('new_investment.html', {
        'investor': request.user,
        'investment': investment,
        'user': portfolio.owner,
        'domain': current_site.domain,
        'portfolio': portfolio
    })
    text_content = strip_tags(html_content)
    to_email = portfolio.owner.email
    email = EmailMultiAlternatives(mail_subject, text_content, 'info@coinium.app', to=[to_email], reply_to=['info@coinium.app'],)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return redirect("/app/portfolio/" + str(portfolio_id))

def newportfolio(request):
    success = 0
    portfolio = None
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.owner = request.user
            portfolio.save()
            success = 1
    else:
        form = PortfolioForm()
    return render(request, 'app/new_portfolio.html', {'form': form, 'success': success, 'portfolio': portfolio})

def portfolio_perf(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk = portfolio_id)
    if request.method == 'GET':
        connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=settings.SPREADS_DB_PASSWD,
                                 db=settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD', 'XXLMZUSD']
                pair_pcts = [float(portfolio.btc_pct) / 100.0, float(portfolio.eth_pct) / 100, float(portfolio.xrp_pct) / 100, float(portfolio.xlm_pct) / 100]
                # pair_pcts = [list_has_distributions[0]["btc"] / 100.0, list_has_distributions[0]["eth"] / 100.0, list_has_distributions[0]["xrp"] / 100.0]
                pair_first_vals = [-1, -1, -1, -1]
                aggr_appreciation_in_pcts = []
                # print("list['created_at']", list['created_at'])
                #start_from_timestamp = time.mktime(datetime.datetime.strptime(list['created_at'], "%Y-%m-%d %H:%M:%S").timetuple())
                # start_from_timestamp = time.mktime(list['created_at'].timetuple())
                # print("start_from_timestamp", start_from_timestamp)
                start_from_timestamp = 1

                until = int(decimal.Decimal(time.time()))
                iteration_time = 1528060609
                #print("iteration_time", iteration_time)
                #print("until", until)
                #print("")

                spreads_for_pair = dict()
                spreads_idx_for_pair = dict()
                for pair in pairs:
                    #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                    sql = """select round(avg((bestbid + bestask) / 2 ),3) as price, convert((min(created_at) div 500)*500, datetime) as time
from Spreads where coin = %s and created_at >= DATE_SUB(curdate(), INTERVAL 6 WEEK)
group by created_at div 500;"""
                    cursor.execute(sql, (pair,))
                    spreads = cursor.fetchall()
                    spreads_for_pair[pair] = spreads
                    spreads_idx_for_pair[pair] = len(spreads) - 1
                    #print("for coin ", pair, " found ", len(spreads), " spreads")

                tm = spreads_for_pair[pairs[0]][0]["time"]
                tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                appreciations = [[tmstmp, 1.0]]
                for i in range(1, len(spreads_for_pair[pairs[0]])):
                    appreciation = 0.0
                    for j in range(len(pairs)):
                        # hack for missing stellar pricing data
                        if j == 3 and i >= len(spreads_for_pair[pairs[j]]):
                            px = 0.5
                        else:
                            px = spreads_for_pair[pairs[j]][i]["price"]
                        # print ("i", i, "px", px)
                        appreciation += pair_pcts[j] * (px / spreads_for_pair[pairs[j]][0]["price"])
                    tm = spreads_for_pair[pairs[0]][i]["time"]
                    tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                    appreciations.append([tmstmp, appreciation])

                # tm = spreads_for_pair[pairs[0]][0]["time"]
                # tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                # dct = {"pointStart":tmstmp,"pointInterval":60000,"dataLength":len(spreads_for_pair[pairs[0]]),"data":appreciations}
                return JsonResponse(appreciations, safe=False)
        finally:
            connection.close()
    return JsonResponse({'error': 'Unsupported method'})

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    investments = Investment.objects.filter(owner=user)
    portfolios = Portfolio.objects.filter(owner=user)
    total_btc = 0.0
    total_eth = 0.0
    total_xrp = 0.0
    total_xlm = 0.0
    for investment in investments:
        total_btc += float(investment.btc_amt)
        total_eth += float(investment.eth_amt)
        total_xrp += float(investment.xrp_amt)
        total_xlm += float(investment.xlm_amt)

    # get latest valuations
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=settings.SPREADS_DB_PASSWD,
                                 db=settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
            spreads_for_pair = dict()
            for pair in pairs:
                #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                sql = "select * from Spreads where coin = %s order by created_at desc limit 1"
                cursor.execute(sql, (pair,))
                spreads = cursor.fetchall()
                spreads_for_pair[pair] = spreads
                #print("for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

            btc_latest_val = float(spreads_for_pair[pairs[0]][0]["bestbid"])
            eth_latest_val = float(spreads_for_pair[pairs[1]][0]["bestbid"])
            xrp_latest_val = float(spreads_for_pair[pairs[2]][0]["bestbid"])
            xlm_latest_val = 0.5
    finally:
        connection.close()

    total_pv_val = btc_latest_val * total_btc + \
                   eth_latest_val * total_eth + \
                   xrp_latest_val * total_xrp + \
                   xlm_latest_val * total_xlm

    if total_pv_val:
        btc_pct = round(100 * btc_latest_val * total_btc / total_pv_val, 2)
        eth_pct = round(100 * eth_latest_val * total_eth / total_pv_val, 2)
        xrp_pct = round(100 * xrp_latest_val * total_xrp / total_pv_val, 2)
        xlm_pct = round(100 * xlm_latest_val * total_xlm / total_pv_val, 2)
    else:
        btc_pct = 0
        eth_pct = 0
        xrp_pct = 0
        xlm_pct = 0

    #calculate investment amounts
    investments_with_amts = []
    # connection = pymysql.connect(host='localhost',
    #                              user='root',
    #                              password=settings.SPREADS_DB_PASSWD,
    #                              db=settings.SPREADS_DB_NAME,
    #                              charset='utf8mb4',
    #                              cursorclass=pymysql.cursors.DictCursor)
    for investment in investments:
        # try:
        #     with connection.cursor() as cursor:
        #         pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
        #         spreads_for_pair = dict()
        #         for pair in pairs:
        #             #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
        #             sql = "select * from Spreads where coin = %s and created_at < %s order by created_at desc limit 1"
        #             cursor.execute(sql, (pair,investment.created_at))#'2018-06-13 18:17:12'))
        #             spreads = cursor.fetchall()
        #             spreads_for_pair[pair] = spreads
        #             #print("for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

        #         btc_latest_val_preceding_investment = float(spreads_for_pair[pairs[0]][0]["bestbid"])
        #         eth_latest_val_preceding_investment = float(spreads_for_pair[pairs[1]][0]["bestbid"])
        #         xrp_latest_val_preceding_investment = float(spreads_for_pair[pairs[2]][0]["bestbid"])
        #         xlm_latest_val_preceding_investment = 0.5
        # finally:
        #     pass

        # amt = float(investment.btc_amt) * btc_latest_val_preceding_investment + \
        # float(investment.eth_amt) * eth_latest_val_preceding_investment + \
        # float(investment.xrp_amt) * xrp_latest_val_preceding_investment + \
        # float(investment.xlm_amt) * xlm_latest_val_preceding_investment
        amt = 0
        investments_with_amts.append([investment, amt])

    # connection.close()

    # investments made to user's portfolios for each month
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=settings.SPREADS_DB_PASSWD,
                                 db=settings.SPREADS_DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    investment_amts_for_months = [0.0] * 13
    all_portfolios_coin_amts_for_individual_months = [[0.0 for i in range(4)] for j in range(13)]
    end_of_month_coin_prices = [[0.0 for i in range(4)] for j in range(13)]
    cur_month = 0
    try:
        with connection.cursor() as cursor:
            sql = "SELECT MONTH(CURDATE()) as month";
            cursor.execute(sql, ())
            cur_month = int(cursor.fetchall()[0]["month"])
            for i in range(0, 3):
                pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
                spreads_for_pair = dict()
                for pair in pairs:
                    sql = "select * from Spreads where coin = %s AND YEAR(created_at) = YEAR(DATE_SUB(CURDATE(), INTERVAL " + str(i-1) + " MONTH)) \
                                            AND MONTH(created_at) < MONTH(DATE_SUB(CURDATE(), INTERVAL " + str(i-1) + " MONTH)) order by created_at desc limit 1"
                    cursor.execute(sql, (pair))
                    spreads = cursor.fetchall()
                    spreads_for_pair[pair] = spreads
                    #print("2 for coin ", pair, " found ", len(spreads), " spreads. spreads:", spreads)

                if len(spreads_for_pair[pairs[0]]) > 0:
                    btc_latest_val_at_the_end_of_the_month = float(spreads_for_pair[pairs[0]][0]["bestbid"])
                else:
                    btc_latest_val_at_the_end_of_the_month = 0.0
                if len(spreads_for_pair[pairs[1]]) > 0:
                    eth_latest_val_at_the_end_of_the_month = float(spreads_for_pair[pairs[1]][0]["bestbid"])
                else:
                    eth_latest_val_at_the_end_of_the_month = 0.0
                if len(spreads_for_pair[pairs[2]]) > 0:
                    xrp_latest_val_at_the_end_of_the_month = float(spreads_for_pair[pairs[2]][0]["bestbid"])
                else:
                    xrp_latest_val_at_the_end_of_the_month = 0.0
                xlm_latest_val_at_the_end_of_the_month = 0.5

                end_of_month_amt = 0.0
                users_portfolios = Portfolio.objects.filter(owner = user)
                portfolio_ids = ["-1"]
                for p in users_portfolios:
                    portfolio_ids.append(str(p.id))
                portfolio_ids_str = ','.join(portfolio_ids)
                for investment in Investment.objects.raw("SELECT * \
                                                FROM app_investment \
                                                WHERE YEAR(created_at) = YEAR(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                                AND MONTH(created_at) = MONTH(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                                AND portfolio_id in (" + portfolio_ids_str + ")"):
                    end_of_month_amt += float(investment.btc_amt) * btc_latest_val_at_the_end_of_the_month + \
                        float(investment.eth_amt) * eth_latest_val_at_the_end_of_the_month + \
                        float(investment.xrp_amt) * xrp_latest_val_at_the_end_of_the_month + \
                        float(investment.xlm_amt) * xlm_latest_val_at_the_end_of_the_month
                    
                    # print("i = ", i, "cur_month = ", cur_month)
                    # print("investment:", investment.btc_amt, investment.eth_amt, investment.xrp_amt, investment.xlm_amt)
                    # print("before all_portfolios_coin_amts_for_individual_months", all_portfolios_coin_amts_for_individual_months)
                    all_portfolios_coin_amts_for_individual_months[cur_month - i][0] += float(investment.btc_amt)
                    all_portfolios_coin_amts_for_individual_months[cur_month - i][1] += float(investment.eth_amt)
                    all_portfolios_coin_amts_for_individual_months[cur_month - i][2] += float(investment.xrp_amt)
                    all_portfolios_coin_amts_for_individual_months[cur_month - i][3] += float(investment.xlm_amt)
                    # print("after all_portfolios_coin_amts_for_individual_months", all_portfolios_coin_amts_for_individual_months)
                end_of_month_coin_prices[cur_month - i][0] = btc_latest_val_at_the_end_of_the_month
                end_of_month_coin_prices[cur_month - i][1] = eth_latest_val_at_the_end_of_the_month
                end_of_month_coin_prices[cur_month - i][2] = xrp_latest_val_at_the_end_of_the_month
                end_of_month_coin_prices[cur_month - i][3] = xlm_latest_val_at_the_end_of_the_month
                # print("end_of_month_amt", end_of_month_amt, "for i = ", i)

                investment_amts_for_months[cur_month - i] = end_of_month_amt

    finally:
        connection.close()
        pass

    # user's portfolios investments and performances over months
    all_portfolios_coin_amts_till_month = [[0.0 for i in range(4)] for j in range(13)]
    end_of_month_usd_amt = [0.0 for i in range(13)]
    investment_in_month_usd_amt = [0.0 for i in range(13)]
    # print("all_portfolios_coin_amts_for_individual_months", all_portfolios_coin_amts_for_individual_months)
    for i in range(1,13):
        all_portfolios_coin_amts_till_month[i][0] = all_portfolios_coin_amts_till_month[i-1][0] + all_portfolios_coin_amts_for_individual_months[i][0]
        all_portfolios_coin_amts_till_month[i][1] = all_portfolios_coin_amts_till_month[i-1][1] + all_portfolios_coin_amts_for_individual_months[i][1]
        all_portfolios_coin_amts_till_month[i][2] = all_portfolios_coin_amts_till_month[i-1][2] + all_portfolios_coin_amts_for_individual_months[i][2]
        all_portfolios_coin_amts_till_month[i][3] = all_portfolios_coin_amts_till_month[i-1][3] + all_portfolios_coin_amts_for_individual_months[i][3]
        end_of_month_usd_amt[i] = all_portfolios_coin_amts_till_month[i][0] * end_of_month_coin_prices[i][0] + \
                                  all_portfolios_coin_amts_till_month[i][1] * end_of_month_coin_prices[i][1] + \
                                  all_portfolios_coin_amts_till_month[i][2] * end_of_month_coin_prices[i][2] + \
                                  all_portfolios_coin_amts_till_month[i][3] * end_of_month_coin_prices[i][3]
        investment_in_month_usd_amt[i] = all_portfolios_coin_amts_for_individual_months[i][0] * end_of_month_coin_prices[i][0] + \
                                         all_portfolios_coin_amts_for_individual_months[i][1] * end_of_month_coin_prices[i][1] + \
                                         all_portfolios_coin_amts_for_individual_months[i][2] * end_of_month_coin_prices[i][2] + \
                                         all_portfolios_coin_amts_for_individual_months[i][3] * end_of_month_coin_prices[i][3]
        #hack:
        end_of_month_usd_amt[i] -= investment_in_month_usd_amt[i]
    # print("all_portfolios_coin_amts_till_month", all_portfolios_coin_amts_till_month)
    # print("end_of_month_usd_amt", end_of_month_usd_amt)
    # print("investment_in_month_usd_amt", investment_in_month_usd_amt)

    # bottom right - all investments by user
    all_investments_by_user_in_original_usd_amt_in_month = [0 for x in range(13)]
    for i in range(0, 3):
        for investment in Investment.objects.raw("SELECT * \
                                              FROM app_investment \
                                              WHERE YEAR(created_at) = YEAR(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                              AND MONTH(created_at) = MONTH(DATE_SUB(CURDATE(), INTERVAL " + str(i) + " MONTH)) \
                                              AND owner_id = " + str(user.id)):
            all_investments_by_user_in_original_usd_amt_in_month[cur_month - i] += investment.original_amt
            

    total_investment_usd_amt = total_btc * end_of_month_coin_prices[cur_month][0] + \
                               total_eth * end_of_month_coin_prices[cur_month][1] + \
                               total_xrp * end_of_month_coin_prices[cur_month][2] + \
                               total_xlm * end_of_month_coin_prices[cur_month][3]
    total_investment_usd_amt = round(total_investment_usd_amt, 2)

    # portfolios with AUM
    portfolios_with_aum = []
    for i in range(len(portfolios)):
        aum = 0.0
        for investment in Investment.objects.raw("SELECT * \
                                              FROM app_investment \
                                              WHERE portfolio_id = " + str(portfolios[i].id)):
            aum += float(investment.original_amt)
        portfolios_with_aum.append([portfolios[i], aum])

    request_user = request.user;
    return render(request, 'app/profile.html', {"user": user, "request_user": request_user, "investments": investments, \
        "investments_with_amts": investments_with_amts,\
        "investment_amts_for_months": investment_amts_for_months,\
        "end_of_month_usd_amt": end_of_month_usd_amt,\
        "investment_in_month_usd_amt": investment_in_month_usd_amt,\
        "all_investments_by_user_in_original_usd_amt_in_month": all_investments_by_user_in_original_usd_amt_in_month,\
        "total_investment_usd_amt": total_investment_usd_amt,\
        "portfolios_with_aum": portfolios_with_aum,\
        "total_pv_val": total_pv_val,\
        "total_btc": total_btc,\
        "total_eth": total_eth,\
        "total_xrp": total_xrp,\
        "total_xlm": total_xlm,\
        "btc_latest_val": btc_latest_val,\
        "eth_latest_val": eth_latest_val,\
        "xrp_latest_val": xrp_latest_val,\
        "xlm_latest_val": xlm_latest_val,\
        "btc_pct": btc_pct,\
        "eth_pct": eth_pct,\
        "xrp_pct": xrp_pct,\
        "xlm_pct": xlm_pct})

def embed_tweet(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if portfolio.owner.id == request.user.id:
        url = request.GET.get('url')
        r = requests.get('https://api.twitter.com/1/statuses/oembed.json?url=' + url)
        res_json = r.json()
        EmbeddedTweet.objects.create(portfolio = portfolio,
                                     owner = request.user,
                                     url = url,
                                     embed_code = res_json['html'])
        request.session["tweet_embedded"] = True
    return redirect("/app/portfolio/" + str(portfolio_id))