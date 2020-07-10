from middlewares.database import (
    execute_fetchone, execute_fetchall, execute_commit)


def insert_workout_history(uid, course_id, total_time,
                           total_distance, time_list, geo_json):
    sql = "INSERT INTO workout_histories (user_id, course_id, total_time, total_distance, time_list, geo_linestring) VALUE (%s, %s, %s, %s, %s, ST_GeomFromGeoJSON(%s));"
    execute_commit(sql, (uid, course_id, total_time,
                         total_distance, time_list, geo_json))

    sql = "SELECT LAST_INSERT_ID();"
    insert_id = execute_fetchone(sql)['LAST_INSERT_ID()']
    return insert_id


def insert_landmark_visit(work_history_id, landmark_id, time):
    sql = "INSERT INTO landmark_visits (workout_history_id, landmark_id, time) VALUE (%s, %s, %s)"
    execute_commit(sql, (work_history_id, landmark_id, time))


def get_shortest(course_id):
    sql = "SELECT MIN(total_time), MIN(total_distance) FROM workout_histories WHERE course_id = %s"
    result = execute_fetchone(sql, (course_id))
    return result


def get_mean_total_record(course_id):
    sql = "SELECT avg(total_time), avg(total_distance) FROM workout_histories WHERE course_id = %s"
    result = execute_fetchone(sql, (course_id))
    return result


def get_totaldist_timelist_poslist(uid, course_id):
    sql = "SELECT id, time_list, ST_AsGeoJSON(geo_linestring), total_distance, total_time FROM workout_histories WHERE user_id = %s AND course_id = %s ORDER BY total_time"
    result = execute_fetchone(sql, (uid, course_id))
    return result


def get_based_on_date(uid, date):
    sql = "SELECT total_time, total_distance, ST_AsGeoJSON(geo_linestring) FROM workout_histories WHERE user_id = %s AND DATE(created_at) = %s"
    result = execute_fetchall(sql, (uid, date))
    return result

def get_by_course_id(cid):
    sql = "SELECT * FROM workout_histories WHERE course_id = %s"
    result = execute_fetchall(sql, (cid))
    return result