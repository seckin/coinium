from flask import Flask
import pymysql
import pymysql.cursors

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='co1n23im',
                                 db='coinim',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Spreads` WHERE `timestamp`<%s"
            cursor.execute(sql, (1600000000,))
            result = cursor.fetchone()
            return str(result)
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')