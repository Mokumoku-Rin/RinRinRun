from db.workout import insert_workout_history, get_workout_history_id, insert_landmark_visit
from db.user import update_user_totaltime


def add_workout_history(uid, course_id, total_time,
                        total_distance, geo_json):
    insert_workout_history(uid, course_id, total_time,
                           total_distance, geo_json)
    # 別関数に分けたり、usecase.userに置くべきかもしれん
    update_user_totaltime(uid, total_time)


def add_landmark_visit(uid, cource_id, geometry_track, time, route):
    work_history_id = get_workout_history_id(
        uid, cource_id, geometry_track, time)
    print("work_history:", work_history_id)
    for i in route:
        landmark_id = 1  # 実際にはlandmarkテーブルからidを取ってくる必要がある
        time = i.time
        insert_landmark_visit(work_history_id['id'], landmark_id, time)
