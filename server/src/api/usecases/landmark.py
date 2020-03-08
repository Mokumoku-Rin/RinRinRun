from db.landmarks import get_landmarks_by_course_id

def get_landmarks_for_course_request(course_id):
  return get_landmarks_by_course_id(course_id)
  