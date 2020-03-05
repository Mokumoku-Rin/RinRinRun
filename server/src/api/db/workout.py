import pymysql.cursors
from middlewares.database import get_db


def insert_workout_history(uid, cource_id, geometry_track, time):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO workout_histories (user_id, cource_id, geometry_track, time) VALUE (%s, %s, %s, %s);"
        cursor.execute(sql, (uid, cource_id, geometry_track, time))
    conn.commit()
