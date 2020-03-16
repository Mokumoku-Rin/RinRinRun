from db.landmark_visit import get_landmark_visit
from db.landmarks import get_landmarks_by_course_id, insert_landmark


def get_landmarks_for_course_request(course_id):
    return get_landmarks_by_course_id(course_id)


def get_landmark_visits_for_ghost(workout_id_list: list) -> list:
    """
    ゴーストの生成に必要なlandmark_visitのデータを workout_idのリストから取得する

    Parameters
    ----------
      workout_id_list: list
        Visitsの対象workout_id
    Returns:
      landmark_visit_list: list
        [
          {
            "id": int
            "time": int
          }...
        ]
    """
    landmark_visit_list = []
    for w_id in workout_id_list:
        l_visit = get_landmark_visit(w_id)
        landmark_visit_list.append(l_visit)

    return landmark_visit_list


def add_landmark(name, description, img_url, pos):
    insert_landmark(name, description, img_url, pos)
    # TODO: 画像をもらって，Firebase Storageに画像を入れる
