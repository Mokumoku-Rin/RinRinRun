import pprint

from usecases.course import get_course_list_by, get_cource
from usecases.landmark import get_landmarks_for_course_request, get_landmark_visits_for_ghost
from usecases.user import get_user_score, get_user_list_by_score_close
from usecases.workout import get_workout_list_for_ghost

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
    course_result = get_cource(course_id)
    landmark_result = get_landmarks_for_course_request(course_id)
    return course_result, landmark_result

  @staticmethod
  def gether_ghost_info_list(uid: str, course_id: int):
    user_score = get_user_score(uid)
    # [{name: str, img_url: str, score: str}] len is 7
    user_info_list = get_user_list_by_score_close(user_score, course_id)
    ghost_uid_list = [u_info["id"] for u_info in user_info_list]
    id_list, ghost_workout_list = get_workout_list_for_ghost(ghost_uid_list, course_id)
    ghost_landmark_visit_list = get_landmark_visits_for_ghost(id_list)

    num_of_ghosts = len(ghost_uid_list)

    ghosts = []
    for i in range(num_of_ghosts):
      user_info = user_info_list[i]
      ghost_workout = ghost_workout_list[i]
      ghost_landmark_visits = ghost_landmark_visit_list[i]

      ghosts.append({
        "name": user_info["name"],
        "img_url": user_info["img_url"],
        "time_list": ghost_workout["time_list"],
        "pos_list": ghost_workout["pos_list"],
        "total_distance": ghost_workout["total_distance"],
        "total_time": ghost_workout["total_time"],
        "landmark_visits": ghost_landmark_visits
      })
    
    print(ghosts)
    return ghosts


