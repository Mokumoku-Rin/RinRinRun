from db.workout import insert_workout_history, insert_landmark_visit
from db.user import update_user_total_record


def add_workout_history(uid, course_id, total_time,
                        total_distance, geo_json):
    insert_id = insert_workout_history(uid, course_id, total_time,
                                       total_distance, geo_json)
    # 別関数に分けたり、usecase.userに置くべきかもしれん
    update_user_total_record(uid, total_time, total_distance)

    return insert_id


def add_landmark_visit(uid, insert_id, landmark_visits):
    for i in landmark_visits:
        landmark_id = i.id
        time = i.time
        insert_landmark_visit(insert_id, landmark_id, time)
