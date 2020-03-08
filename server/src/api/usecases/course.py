from db.course import get_course_list_by_popular, get_course_list_by_latest, get_course_by_id

def get_course_list_by(order: str, limit: int):
  result = {}
  if order == "popular":
    result = get_course_list_by_popular(limit)
  elif order == "latest":
    result = get_course_list_by_latest(limit)

  return result

def get_cource(course_id: int):
  return get_course_by_id(course_id)
