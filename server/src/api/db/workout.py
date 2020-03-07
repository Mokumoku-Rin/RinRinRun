import pymysql.cursors
from middlewares.database import get_db


def insert_workout_history(uid, course_id, total_time,
                           total_distance, geo_json):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO workout_histories (user_id, cource_id, total_time, total_distance, geo_linestring) VALUE (%s, %s, %s, %s, ST_GeomFromGeoJSON(%s));"
        cursor.execute(sql, (uid, course_id, total_time,
                             total_distance, geo_json))
    conn.commit()


def get_workout_history_id(uid, cource_id, geometry_track, time):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT id FROM workout_histories WHERE user_id = %s and cource_id = %s and geometry_track = %s and time = %s"
        cursor.execute(sql, (uid, cource_id, geometry_track, time))
        result = cursor.fetchone()
    return result


def insert_landmark_visit(work_history_id, landmark_id, time):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO landmark_visits (workout_history_id, landmark_id, time) VALUE (%s, %s, %s)"
        cursor.execute(sql, (work_history_id, landmark_id, time))
    conn.commit()
