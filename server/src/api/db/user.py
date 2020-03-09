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


def get_user_score(uid) -> int:
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT score FROM users WHERE id = %s"
        cursor.execute(sql, (uid))
        result = cursor.fetchone()["score"]
    return int(result)

def get_users_name_img_by_score_and_course_done(user_score, course_id, limit: int) -> list:
    """
    与えられたユーザスコアから近い順かつ，指定のコースを走ったことのあるユーザをにlimit個のゴーストに必要なデータを取得する
    Returns
    -------
        result: list
            [
                {id: str, name: str, img_url: str},
                {id: str, name: str, img_url: str},
                ...
            ]
    """
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT users.id, users.name, users.img_url FROM users JOIN workout_histories ON users.id = workout_histories.user_id WHERE workout_histories.course_id = %s ORDER BY ABS(users.score - %s) LIMIT %s"
        cursor.execute(sql, (course_id, user_score, limit))
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
