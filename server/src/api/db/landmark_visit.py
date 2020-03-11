import pymysql.cursors
from middlewares.database import get_db


def get_landmark_visit(workout_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT landmark_id, time FROM landmark_visits WHERE workout_history_id = %s"
        cursor.execute(sql, (workout_id))
        result = cursor.fetchall()
    return result
