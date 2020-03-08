import pymysql.cursors
from middlewares.database import get_db


def update_mean_record(mean_time, mean_distance, course_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = 'UPDATE courses SET mean_time = %s, mean_distance = %s WHERE id = %s'
        cursor.execute(sql, (mean_time, mean_distance, course_id))
    conn.commit()
