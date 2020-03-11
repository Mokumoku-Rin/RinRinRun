from middlewares.database import (
    execute_fetchone, execute_fetchall, execute_commit)


def insert_user(uid, name, img_url):
    sql = "INSERT INTO users (id, name, img_url) VALUES(%s, %s, %s);"
    execute_commit(sql, (uid, name, img_url))


def get_user(uid):
    sql = "SELECT id FROM users WHERE id = %s"
    result = execute_fetchall(sql, (uid))
    return result


def get_user_score(uid) -> int:
    sql = "SELECT score FROM users WHERE id = %s"
    result = execute_fetchone(sql, (uid))["score"]
    return int(result)


def get_users_name_img_by_score_and_course_done(user_score, course_id, limit: int) -> list:
    """
    与えられたユーザスコアから近い順かつ，指定のコースを走ったことのあるユーザをにlimit個のゴーストに必要なデータを取得する
    Returns
    -------
        result: list
            [
                {id: str, name: str, img_url: str},
                {id: str, name: str, img_url: str},
                ...
            ]
    """
    sql = "SELECT DISTINCT users.id, users.name, users.img_url FROM users LEFT JOIN workout_histories ON users.id = workout_histories.user_id WHERE workout_histories.course_id = %s ORDER BY ABS(users.score - %s) LIMIT %s"
    result = execute_fetchall(sql, (course_id, user_score, limit))
    return result


def update_user_total_record(uid, time, distance):
    sql = "UPDATE users SET total_time = total_time + %s, total_distance = total_distance + %s  WHERE id = %s"
    execute_commit(sql, (time, distance, uid))


def update_user_totaldistance(uid, total_distance):
    sql = "UPDATE users SET total_distance = total_distance + %s WHERE id = %s"
    execute_commit(sql, (total_distance, uid))
