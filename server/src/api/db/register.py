import pymysql.cursors
from usecases.connectiondb import get_db_connection

def register(conn, uid):
    with conn.cursor() as cursor:
        sql = "INSERT INTO users VALUES(%s, default, default, default, default, default);"
        cursor.execute(sql, (uid,))
    conn.commit()


def check_register(uid):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = "SELECT id FROM users WHERE id = %s"
        cursor.execute(sql, (uid,))
        result = cursor.fetchall()
    if result:
        return True
    register(conn, uid)
    return False