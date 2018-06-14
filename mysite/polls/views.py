from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from .models import Choice, Question, Portfolio
from .forms import PortfolioForm
import pymysql
import pymysql.cursors
import decimal
import time
import datetime


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
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
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def portfolio(request, pk):
    all_portfolios = Portfolio.objects.all()
    portfolio = Portfolio.objects.get(pk=pk)
    return render(request, 'polls/portfolio.html', {'all_portfolios': all_portfolios, 'pk': pk, 'portfolio': portfolio})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

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
    return render(request, 'polls/new_portfolio.html', {'form': form, 'success': success, 'portfolio': portfolio})

def portfolio_perf(request):
    if request.method == 'GET':
        connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='01990199',
                                 db='coinium',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
                pair_pcts = [0.30, 0.30, 0.40]
                # pair_pcts = [list_has_distributions[0]["btc"] / 100.0, list_has_distributions[0]["eth"] / 100.0, list_has_distributions[0]["xrp"] / 100.0]
                pair_first_vals = [-1, -1, -1]
                aggr_appreciation_in_pcts = []
                # print("list['created_at']", list['created_at'])
                #start_from_timestamp = time.mktime(datetime.datetime.strptime(list['created_at'], "%Y-%m-%d %H:%M:%S").timetuple())
                # start_from_timestamp = time.mktime(list['created_at'].timetuple())
                # print("start_from_timestamp", start_from_timestamp)
                start_from_timestamp = 1

                until = int(decimal.Decimal(time.time()))
                iteration_time = 1528060609
                print("iteration_time", iteration_time)
                print("until", until)
                print("")

                spreads_for_pair = dict()
                spreads_idx_for_pair = dict()
                for pair in pairs:
                    #sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                    sql = """select round(avg((bestbid + bestask) / 2 ),3) as price, convert((min(created_at) div 100)*100, datetime) as time
from Spreads where coin = %s and created_at >= '2018-05-19 04:12:14' AND created_at <= '2018-05-25 04:12:14'
group by created_at div 100;"""
                    cursor.execute(sql, (pair,))
                    spreads = cursor.fetchall()
                    spreads_for_pair[pair] = spreads
                    spreads_idx_for_pair[pair] = len(spreads) - 1
                    print("for coin ", pair, " found ", len(spreads), " spreads")

                tm = spreads_for_pair[pairs[0]][0]["time"]
                tmstmp = round(time.mktime(tm.timetuple()) * 1000)
                appreciations = [[tmstmp, 1.0]]
                for i in range(1, len(spreads_for_pair[pairs[0]])):
                    appreciation = 0.0
                    for j in range(len(pairs)):
                        appreciation += pair_pcts[j] * (spreads_for_pair[pairs[j]][i]["price"] / spreads_for_pair[pairs[j]][0]["price"])
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

