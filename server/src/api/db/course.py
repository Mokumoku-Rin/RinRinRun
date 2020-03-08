import pymysql.cursors
from middlewares.database import get_db


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
