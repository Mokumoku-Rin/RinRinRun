from db.workout import insert_workout_history, insert_landmark_visit, get_mean_total_record
from db.user import update_user_total_record
from db.course import update_mean_record, update_played_count


def add_workout_history(uid, course_id, total_time,
                        total_distance, time_list, geo_json):
    insert_id = insert_workout_history(uid, course_id, total_time,
                                       total_distance, time_list, geo_json)
    # 別関数に分けたり、usecase.userに置くべきかもしれん
    update_user_total_record(uid, total_time, total_distance)

    return insert_id


def add_landmark_visit(uid, insert_id, landmark_visits):
    for i in landmark_visits:
        landmark_id = i.id
        time = i.time
        insert_landmark_visit(insert_id, landmark_id, time)


def update_course_mean_record(course_id, total_time, total_distance):
    mean_data = get_mean_total_record(course_id)
    update_mean_record(mean_data['avg(total_time)'],
                       mean_data['avg(total_distance)'], course_id)


def update_course_play_count(course_id):
    update_played_count(course_id)
