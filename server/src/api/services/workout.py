from usecases.auth import verify_token
from usecases.workout import add_workout_history, add_landmark_visit
from usecases.user import update_user_record

from schemas.workout import WorkoutRequest


class WorkoutService:
    @staticmethod
    async def workout_test(workout_request, uid):
        cource_id = workout_request.course_id
        geometry_track = workout_request.move_history
        time = workout_request.total_time
        route = workout_request.route
        add_workout_history(uid, cource_id, geometry_track, time)
        add_landmark_visit(uid, cource_id, geometry_track, time, route)
        return geometry_track

    @staticmethod
    async def new_record(uid: str, workout_request: WorkoutRequest):
        props = workout_request.properties
        geo = workout_request.geo_json
        visits =workout_request.landmark_visits

        update_user_record(props.dict()["total_time"])
