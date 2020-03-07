from usecases.auth import verify_token
from usecases.workout import add_workout_history, add_landmark_visit, update_user_totaltime


class WorkoutService:
    @staticmethod
    async def workout_test(workout_request, uid):
        properties = workout_request.properties
        time_list = properties.time_list
        total_distance = properties.total_distance
        total_time = properties.total_time
        course_id = properties.course_id
        landmark_visits = workout_request.landmark_visits
        geo_json = workout_request.geo_json

        add_workout_history(uid, course_id, total_time,
                            total_distance, geo_json)
        add_landmark_visit(uid, course_id, total_time,
                           total_distance, geo_json, landmark_visits)

        return "OK"
