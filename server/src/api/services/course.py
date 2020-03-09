from usecases.course import get_course_list_by, get_course
from usecases.landmark import get_landmarks_for_course_request

class CourseService:
  @staticmethod
  def get_by_id(id: int):
    pass

  @staticmethod
  def get_course_list(sorted: str, limit: int):
    result = get_course_list_by(sorted, limit)
    return result
  
  @staticmethod
  def gether_course_info(course_id: int):
    course_result = get_course(course_id)
    landmark_result = get_landmarks_for_course_request(course_id)
    return course_result, landmark_result
