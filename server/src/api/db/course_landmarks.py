from middlewares.database import (execute_commit, execute_fetchall,
                                  execute_fetchone)


def insert_landmarks(id, landmarks):
    sql = 'INSERT INTO course_landmarks (course_id, landmark_id)' \
        'VALUES (%s, %s)'
    execute_commit(sql, (id, landmarks))
    return "OK"
