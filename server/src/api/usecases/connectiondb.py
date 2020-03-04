import pymysql.cursors
import os

def get_db_connection():
    conn = pymysql.connect(
                    host='mokumoku-mariadb',
                    user=os.environ['DB_USER'],
                    passwd=os.environ['DB_PASSWORD'],
                    db='mokumoku',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)
    return conn