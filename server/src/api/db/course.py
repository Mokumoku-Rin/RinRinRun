from middlewares.database import (
    execute_fetchone, execute_fetchall, execute_commit)


def get_course_list_by_popular(limit: int):
    sql = "SELECT id, name, description FROM courses" + \
          _build_order_by("played_count", limit)
    result = execute_fetchall(sql)
    return result


def get_course_list_by_latest(limit: int):
    sql = "SELECT id, name, description FROM courses" + \
          _build_order_by("created_at", limit)
    result = execute_fetchall(sql)
    return result


def get_course_by_id(course_id: int):
    sql = "SELECT id, name, description, mean_distance, mean_time FROM courses WHERE id = %s"
    result = execute_fetchone(sql, (course_id))
    return result


def _build_order_by(order: str, limit: int):
    return " ORDER BY %s limit %s" % (order, limit)


def update_mean_record(mean_time, mean_distance, course_id):
    sql = 'UPDATE courses SET mean_time = %s, mean_distance = %s WHERE id = %s'
    execute_commit(sql, (mean_time, mean_distance, course_id))


def update_played_count(course_id):
    sql = 'UPDATE courses SET played_count = played_count + 1 WHERE id = %s'
    execute_commit(sql, (course_id))
