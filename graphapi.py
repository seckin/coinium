from flask import Flask
from flask import request
import pymysql
import pymysql.cursors
import decimal
import time
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    #return "<h1 style='color:blue'>Hello There!</h1>"
    list_id = request.args.get('list_id')
    interval_in_secs = request.args.get('interval_in_secs')
    if not interval_in_secs:
        interval_in_secs = 30
    else:
        interval_in_secs = int(interval_in_secs)
    print("interval_in_secs", interval_in_secs)
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='co1n23im',
                                 db='coinim',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            #list_id = 1
            sql = "SELECT * FROM Lists WHERE `id`=%s"
            # sql = "SELECT * FROM `ListHasDistribution` WHERE `list_id`=%s"
            cursor.execute(sql, (list_id,))
            list = cursor.fetchone()

            sql = """SELECT a.list_id, a.distribution_id, a.timestamp, b.btc, b.eth, b.xrp
                FROM ListHasDistribution a LEFT JOIN Distributions b
                ON a.distribution_id = b.id
                WHERE `list_id`=%s"""
            # sql = "SELECT * FROM `ListHasDistribution` WHERE `list_id`=%s"
            cursor.execute(sql, (list_id,))
            list_has_distributions = cursor.fetchall()


            #assume distribution doesn't change for now:
            # list_has_distributions[0]["btc"] #30
            #    since = int(decimal.Decimal(time.time()))
            # since -= 30

            pairs = ['XXBTZUSD', 'XETHZUSD', 'XXRPZUSD']
            #pair_pcts = [0.30, 0.30, 0.40]
            pair_pcts = [list_has_distributions[0]["btc"] / 100.0, list_has_distributions[0]["eth"] / 100.0, list_has_distributions[0]["xrp"] / 100.0]
            pair_first_vals = [-1, -1, -1]
            aggr_appreciation_in_pcts = []
            print("list['created_at']", list['created_at'])
            #start_from_timestamp = time.mktime(datetime.datetime.strptime(list['created_at'], "%Y-%m-%d %H:%M:%S").timetuple())
            start_from_timestamp = time.mktime(list['created_at'].timetuple())
            print("start_from_timestamp", start_from_timestamp)

            until = int(decimal.Decimal(time.time()))
            iteration_time = 1527016686
            print("iteration_time", iteration_time)
            print("until", until)
            print("")

            spreads_for_pair = dict()
            spreads_idx_for_pair = dict()
            for pair in pairs:
                sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                cursor.execute(sql, (pair, start_from_timestamp,))
                spreads = cursor.fetchall()
                spreads_for_pair[pair] = spreads
                spreads_idx_for_pair[pair] = len(spreads) - 1
                print("for coin ", pair, " found ", len(spreads), " spreads")
            while iteration_time < until:
                i = 0
                aggr_appreciation_in_pct = 0
                for pair in pairs:
                    # print("pair", pair)

                    while spreads_idx_for_pair[pair] < len(spreads_for_pair[pair]) - 1 and spreads_for_pair[pair][spreads_idx_for_pair[pair]]["timestamp"] <= iteration_time:
                        spreads_idx_for_pair[pair] += 1

                    while spreads_idx_for_pair[pair] > 0 and spreads_for_pair[pair][spreads_idx_for_pair[pair]]["timestamp"] > iteration_time:
                        # print('spreads[j]["timestamp"]', spreads[j]["timestamp"], " iteration_time", iteration_time)
                        # j -= 1
                        spreads_idx_for_pair[pair] -= 1

                    j = spreads_idx_for_pair[pair]
                    # print("iteration_time", iteration_time)
                    # print('found spread: spreads[j]["timestamp"] = ', spreads_for_pair[pair][j]["timestamp"])
                    # print("spread:", spreads_for_pair[pair][j])
                    start_from_timestamp = spreads_for_pair[pair][j]["timestamp"]

                    bid = float(spreads_for_pair[pair][j]["bestbid"])
                    ask = float(spreads_for_pair[pair][j]["bestask"])
                    last_mid_mkt = (bid + ask) / 2
                    # print("last_mid_mkt", last_mid_mkt)
                    if pair_first_vals[i] == -1:
                        pair_first_vals[i] = last_mid_mkt
                    appreciation_in_pct = last_mid_mkt / pair_first_vals[i]
                    # print("appreciation_in_pct", appreciation_in_pct)
                    # print("")
                    aggr_appreciation_in_pct += pair_pcts[i] * appreciation_in_pct
                    i += 1
                aggr_appreciation_in_pcts.append([iteration_time, aggr_appreciation_in_pct])
                iteration_time += interval_in_secs

            return str(aggr_appreciation_in_pcts)
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')