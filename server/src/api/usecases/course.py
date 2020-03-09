from db.course import get_course_list_by_popular, get_course_list_by_latest, get_course_by_id
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
  course_info.update(shortest_time=workout_shortest['MIN(total_time)'],
                     shortest_distance=workout_shortest['MIN(total_distance)'])
  return course_info
