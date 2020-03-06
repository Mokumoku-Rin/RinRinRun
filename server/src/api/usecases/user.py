from db.user import get_user, insert_user


def is_existed_user(uid):
    user = get_user(uid)
    if user:
        return True
    return False


def add_user(uid, name, img_url):
    insert_user(uid, name, img_url)
