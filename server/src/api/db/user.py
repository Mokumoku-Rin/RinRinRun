import pymysql.cursors
from middlewares.database import get_db
from db.tools import build_update_sql, exec, TABLE


def insert_user(uid):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO users VALUES(%s, default, default, default, default, default);"
        cursor.execute(sql, (uid,))
    conn.commit()


def get_user(uid):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT id FROM users WHERE id = %s"
        cursor.execute(sql, (uid,))
        result = cursor.fetchall()
    return result

def update_user_by_id(uid, name = None, img_url = None, score = None, total_distance = None, total_time = None):
    wheres = "uid = %s" % uid
    sql = build_update_sql({
        name,
        img_url,
        score,
        total_time,
        total_distance
    }, TABLE.USERS, wheres)
    print(sql)
    exec(sql)

def update_user_totaltime(uid, time):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "UPDATE users SET total_time = total_time + %s WHERE id = %s"
        cursor.execute(sql, (time, uid))
    conn.commit()
