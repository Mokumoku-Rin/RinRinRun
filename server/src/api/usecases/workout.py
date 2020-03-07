from db.workout import insert_workout_history, get_workout_history_id, insert_landmark_visit
from db.user import update_user_total_record


def add_workout_history(uid, course_id, total_time,
                        total_distance, geo_json):
    insert_workout_history(uid, course_id, total_time,
                           total_distance, geo_json)
    # 別関数に分けたり、usecase.userに置くべきかもしれん
    update_user_total_record(uid, total_time, total_distance)


def add_landmark_visit(uid, course_id, total_time,
                       total_distance, geo_json, landmark_visits):
    work_history_id = get_workout_history_id(
        uid, course_id, total_time,
        total_distance, geo_json)
    print("work_history:", work_history_id)
    for i in landmark_visits:
        landmark_id = i.id
        time = i.time
        insert_landmark_visit(work_history_id['id'], landmark_id, time)
