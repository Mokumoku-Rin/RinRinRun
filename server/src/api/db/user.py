import pymysql.cursors
from usecases.connectiondb import get_db_connection

def register_user(uid):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "INSERT INTO users VALUES(%s, default, default, default, default, default);"
        cursor.execute(sql, (uid,))
    conn.commit()


def get_user(uid):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "SELECT id FROM users WHERE id = %s"
        cursor.execute(sql, (uid,))
        result = cursor.fetchall()
    return result