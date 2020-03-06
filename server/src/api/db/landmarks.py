import pymysql.cursors
from middlewares.database import get_db


def get_image_url(landmark_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT img_url FROM landmarks WHERE id = %s"
        cursor.execute(sql, (landmark_id,))
        result = cursor.fetchone()
    return result
