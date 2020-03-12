from db.user import (get_user, get_user_score,
                     get_users_name_img_by_score_and_course_done, insert_user)


def is_existed_user(uid):
    user = get_user(uid)
    if user:
        return True
    return False


def add_user(uid, name, img_url):
    insert_user(uid, name, img_url)


def get_user_list_by_score_close(user_score: str, course_id: str) -> list:
    """
    ユーザスコアが近く，かつ指定のコースIDを走ったユーザの情報リストをゴースト用に整形して返す

    Parameters
    ----------
        user_score : 対象ユーザのスコア
        course_id : 対象コースID

    Returns
    -------
        user_list : list
            [
                {id: str, name: str, img_url: str
            ]
    """
    user_list = get_users_name_img_by_score_and_course_done(
        user_score, course_id, 7)
    return user_list
