from flask import Flask
import pymysql
import pymysql.cursors
import decimal
import time
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    #return "<h1 style='color:blue'>Hello There!</h1>"
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='co1n23im',
                                 db='coinim',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            list_id = 1
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

            pairs = ['XETHZUSD', 'XXRPZUSD','XXBTZUSD']
            pair_pcts = [0.30, 0.30, 0.40]
            pair_first_vals = [-1, -1, -1]
            aggr_appreciation_in_pcts = []
            print("list['created_at']", list['created_at'])
            #start_from_timestamp = time.mktime(datetime.datetime.strptime(list['created_at'], "%Y-%m-%d %H:%M:%S").timetuple())
            start_from_timestamp = time.mktime(list['created_at'].timetuple())
            print("start_from_timestamp", start_from_timestamp)

            until = int(decimal.Decimal(time.time()))
            iteration_time = 1527031271
            print("iteration_time", iteration_time)
            print("until", until)
            print("")
            while iteration_time < until:
                i = 0
                aggr_appreciation_in_pct = 0
                for pair in pairs:
                    print("pair", pair)

                    sql = "SELECT * FROM `Spreads` WHERE `coin`=%s AND `timestamp`>=%s ORDER BY `timestamp` asc"
                    cursor.execute(sql, (pair, start_from_timestamp,))
                    spreads = cursor.fetchall()
                    print("for coin ", pair, " found ", len(spreads), " spreads")

                    j = len(spreads) - 1
                    while spreads[j]["timestamp"] > iteration_time:
                        # print('spreads[j]["timestamp"]', spreads[j]["timestamp"], " iteration_time", iteration_time)
                        j -= 1
                    print("iteration_time", iteration_time)
                    print('found spread: spreads[j]["timestamp"] = ', spreads[j]["timestamp"])
                    print("spread:", spreads[j])
                    start_from_timestamp = spreads[j]["timestamp"]
                    start_from_timestamp -= 500 # hack: so that one coin doesn't make another coin fastforward

                    bid = float(spreads[j]["bestbid"])
                    ask = float(spreads[j]["bestask"])
                    last_mid_mkt = (bid + ask) / 2
                    print("last_mid_mkt", last_mid_mkt)
                    if pair_first_vals[i] == -1:
                        pair_first_vals[i] = last_mid_mkt
                    appreciation_in_pct = last_mid_mkt / pair_first_vals[i]
                    print("appreciation_in_pct", appreciation_in_pct)
                    print("")
                    aggr_appreciation_in_pct += pair_pcts[i] * appreciation_in_pct
                    i += 1
                aggr_appreciation_in_pcts.append([iteration_time, aggr_appreciation_in_pct])
                iteration_time += 30

            return str(aggr_appreciation_in_pcts)
            # return str(list)
            # return str(list) + str(list_has_distributions) + str(spreads)
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')