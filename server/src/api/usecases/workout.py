import json

from db.course import update_mean_record, update_played_count
from db.user import update_user_total_record
from db.workout import (get_based_on_date, get_mean_total_record,
                        get_totaldist_timelist_poslist, insert_landmark_visit,
                        insert_workout_history,
                        get_by_course_id)


def get_workout_list_for_ghost(uid_list, course_id) -> (list, list):
    """
    ゴーストのためのワークアウト基礎データを返却する

    Parameters
    ----------
    uid_list : str
        対象ユーザIDリスト
    course_id : str
        対象コースID

    Returns
    -------
    workout_list : list of ghost_workout_info
        [
            {
                "time\_list": [int, int, ... ,int],
                "pos_list": [[float, float], [float, float], ...],
                "total_distance": int
                "total_time": int
            }
        ]
    workout_ids: list of id
    """

    workout_list = []
    id_list = []

    for uid in uid_list:
        raw_ghost_workout = get_totaldist_timelist_poslist(uid, course_id)
        ghost_workout = {}

        # append workout_id
        id_list.append(raw_ghost_workout["id"])

        # set total_distance total_time time_list
        ghost_workout["total_distance"] = int(
            raw_ghost_workout["total_distance"])
        ghost_workout["total_time"] = int(raw_ghost_workout["total_time"])
        ghost_workout["time_list"] = [
            int(t) for t in raw_ghost_workout["time_list"].split(",")]

        # parse pos_list
        ghost_workout["pos_list"] = []
        geojson = json.loads(raw_ghost_workout["ST_AsGeoJSON(geo_linestring)"])

        for pos in geojson["coordinates"]:
            ghost_workout["pos_list"].append(pos)

        workout_list.append(ghost_workout)

    return id_list, workout_list


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


def update_course_status(course_id, total_time, total_distance):
    mean_data = get_mean_total_record(course_id)
    update_mean_record(mean_data['avg(total_time)'],
                       mean_data['avg(total_distance)'], course_id)
    update_played_count(course_id)


def select_history_based_on_date(uid, date):
    # uid = 2
    workout_history_based_on_date = []
    for i in get_based_on_date(uid, date):
        i['geo_json'] = json.loads(i.pop('ST_AsGeoJSON(geo_linestring)'))
        workout_history_based_on_date.append(i)
    return workout_history_based_on_date

def get_all_by_course_id(cid):
    workouts = get_by_course_id(cid)
    if len(workouts) == 0:
        return []

    needed = []
    for workout in workouts:
        needed.append({
            "user_id": workout["user_id"],
            "total_time": workout["total_time"],
            "total_distance": workout["total_distance"]
        })
    return needed