from db.course import (get_course_by_id, get_course_list_by_latest,
                       get_course_list_by_popular, insert_course)
from db.course_landmarks import insert_landmarks
from db.workout import get_shortest


def get_course_list_by(order: str, limit: int):
    result = {}
    if order == "popular":
        result = get_course_list_by_popular(limit)
    elif order == "latest":
        result = get_course_list_by_latest(limit)

    return result


def get_course(course_id: int):
    course_info = get_course_by_id(course_id)
    workout_shortest = get_shortest(course_id)
    if workout_shortest:
        course_info.update(
            shortest_time=workout_shortest['MIN(total_time)'],
            shortest_distance=workout_shortest['MIN(total_distance)']
        )
    return course_info


def add_course(name, description):
    insert_id = insert_course(name, description)
    return insert_id


def add_course_landmarks(course_id, landmarks):
    for i in landmarks:
        insert_landmarks(course_id, i)
    return "OK"
