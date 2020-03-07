from usecases.auth import verify_token
from usecases.workout import add_workout_history, add_landmark_visit, update_user_totaltime


class WorkoutService:
    @staticmethod
    async def add_record(workout_request, uid):
        time_list = workout_request.properties.time_list
        total_distance = workout_request.properties.total_distance
        total_time = workout_request.properties.total_time
        course_id = workout_request.properties.course_id

        landmark_visits = workout_request.landmark_visits
        geo_json = workout_request.geo_json

        add_workout_history(uid, course_id, total_time,
                            total_distance, geo_json)
        add_landmark_visit(uid, course_id, total_time,
                           total_distance, geo_json, landmark_visits)

        return "OK"
