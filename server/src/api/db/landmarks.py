from middlewares.database import (
    execute_fetchone, execute_fetchall, execute_commit)


def get_image_url(landmark_id):
    sql = "SELECT img_path FROM landmarks WHERE id = %s"
    result = execute_fetchone(sql, (landmark_id))
    return result


def get_landmarks_by_course_id(course_id: int):
    sql = 'SELECT landmarks.id, landmarks.name, landmarks.description, landmarks.img_path, landmarks.pos FROM landmarks JOIN course_landmarks ON landmarks.id = course_landmarks.landmark_id JOIN courses ON course_landmarks.course_id = courses.id WHERE courses.id = %s'
    result = execute_fetchall(sql, (str(course_id)))
    return result

def get_landmarks(limit: int):
    sql = 'SELECT id, name, pos, img_path, description FROM landmarks'
    # FIXME: LIMIT区にintを投げるとSQL Syntax Errorが起こる．
    result = execute_fetchall(sql)
    return result

def insert_landmark(name, description, img_path, pos):
    sql = 'INSERT INTO landmarks (name, description, img_path, pos) VALUES (%s, %s, %s, %s)'
    execute_commit(sql, (name, description, img_path, pos))
