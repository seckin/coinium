#https://api.kraken.com/0/public/Spread?pair=XBTUSD

pairs = ['XETHZUSD', 'XXRPZUSD', 'XXBTZUSD']

import krakenex
import decimal
import time
import pymysql
import pymysql.cursors

k = krakenex.API()

since = int(decimal.Decimal(time.time()))
since -= 30
print("since", since)
i = 0
# aggr_last_mid_mkt = 0
for pair in pairs:
    print("pair", pair)
    ret = k.query_public('Spread', data = {'pair': pair, 'since': since})
    print("ret", ret)
    timestamp = int(ret['result'][pair][-1][0])
    bestbid = float(ret['result'][pair][-1][1])
    bestask = float(ret['result'][pair][-1][2])
    print("bestbid", bestbid, "bestask", bestask)
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='co1n23im',
                                 db='coinim',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Spreads` (`coin`, `bestbid`, `bestask`, `timestamp`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (pair, bestbid, bestask, timestamp,))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Spreads` WHERE `timestamp`=%s"
            cursor.execute(sql, (timestamp,))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()