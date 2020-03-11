from middlewares.database import (
    execute_fetchone, execute_fetchall, execute_commit)


def get_landmark_visit(workout_id):
    sql = "SELECT landmark_id, time FROM landmark_visits WHERE workout_history_id = %s"
    result = execute_fetchall(sql, (workout_id))
    return result
