import pymysql.cursors
from middlewares.database import get_db


def get_image_url(landmark_id):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = "SELECT img_url FROM landmarks WHERE id = %s"
        cursor.execute(sql, (landmark_id,))
        result = cursor.fetchone()
    return result


def get_landmarks_by_course_id(course_id: int):
    conn = get_db()
    with conn.cursor() as cursor:
        sql = 'select landmarks.id, landmarks.name, landmarks.description, landmarks.img_url, landmarks.pos from landmarks join course_landmarks on landmarks.id = course_landmarks.landmark_id join courses on course_landmarks.course_id = courses.id WHERE courses.id = %s'
        cursor.execute(sql, (str(course_id),))
        result = cursor.fetchall()
    return result
    