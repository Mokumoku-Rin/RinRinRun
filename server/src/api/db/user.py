import pymysql.cursors
from middlewares.database import get_db


def insert_user(uid, name, img_url):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO users (id, name, img_url) VALUES(%s, %s, %s);"
        cursor.execute(sql, (uid, name, img_url))
    conn.commit()


def get_user(uid):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT id FROM users WHERE id = %s"
        cursor.execute(sql, (uid,))
        result = cursor.fetchall()
    return result


def update_user_total_record(uid, time, distance):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "UPDATE users SET total_time = total_time + %s, total_distance = total_distance + %s  WHERE id = %s"
        cursor.execute(sql, (time, distance, uid))
    conn.commit()


def update_user_totaldistance(uid, total_distance):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "UPDATE users SET total_distance = total_distance + %s WHERE id = %s"
        cursor.execute(sql, (total_distance, uid))
    conn.commit()
