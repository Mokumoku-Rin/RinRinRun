import pymysql.cursors
from middlewares.database import get_db


def get_course_list_by_popular(limit: int):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT id, name, description FROM courses" + \
            _build_order_by("played_count", limit)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def get_course_list_by_latest(limit: int):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT id, name, description FROM courses" + \
            _build_order_by("created_at", limit)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def get_course_by_id(course_id: int):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT id, name, description, mean_distance, mean_time FROM courses WHERE id = %s"
        cursor.execute(sql, (course_id,))
        result = cursor.fetchone()
    return result


def _build_order_by(order: str, limit: int):
    return " ORDER BY %s limit %s" % (order, limit)


def update_mean_record(mean_time, mean_distance, course_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = 'UPDATE courses SET mean_time = %s, mean_distance = %s WHERE id = %s'
        cursor.execute(sql, (mean_time, mean_distance, course_id))
    conn.commit()


def update_played_count(course_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = 'UPDATE courses SET played_count = played_count + 1 WHERE id = %s'
        cursor.execute(sql, (course_id))
    conn.commit()
