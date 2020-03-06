from db.user import get_user, insert_user, update_user_by_id


def is_existed_user(uid):
    user = get_user(uid)
    if user:
        return True
    return False


def add_user(uid):
    insert_user(uid)

def update_user_record(total_time: int, total_distance: int):
    # todo calc score
    score = 100    
    update_user_by_id(score=score, total_distance=total_distance, total_time=total_time)
