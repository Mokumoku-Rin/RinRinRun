import pymysql.cursors
from middlewares.database import get_db


def insert_workout_history(uid, course_id, total_time,
                           total_distance, time_list, geo_json):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO workout_histories (user_id, course_id, total_time, total_distance, time_list, geo_linestring) VALUE (%s, %s, %s, %s, %s, ST_GeomFromGeoJSON(%s));"
        cursor.execute(sql, (uid, course_id, total_time,
                             total_distance, time_list, geo_json))
        sql = "SELECT LAST_INSERT_ID();"
        cursor.execute(sql)

        insert_id = cursor.fetchone()['LAST_INSERT_ID()']
    conn.commit()

    return insert_id


def insert_landmark_visit(work_history_id, landmark_id, time):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO landmark_visits (workout_history_id, landmark_id, time) VALUE (%s, %s, %s)"
        cursor.execute(sql, (work_history_id, landmark_id, time))
    conn.commit()


def get_mean_total_record(course_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT avg(total_time), avg(total_distance) FROM workout_histories WHERE course_id = %s"
        cursor.execute(sql, (course_id))
        result = cursor.fetchone()
    return result
