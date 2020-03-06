from db.workout import insert_workout_history, get_workout_history_id, insert_landmark_visit


def add_workout_history(uid, cource_id, geometry_track, time):
    insert_workout_history(uid, cource_id, geometry_track, time)


def add_landmark_visit(uid, cource_id, geometry_track, time, route):
    work_history_id = get_workout_history_id(
        uid, cource_id, geometry_track, time)
    print("work_history:", work_history_id)
    for i in route:
        landmark_id = 1  # 実際にはlandmarkテーブルからidを取ってくる必要がある
        time = i.time
        insert_landmark_visit(work_history_id['id'], landmark_id, time)
