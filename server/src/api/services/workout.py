from usecases.auth import verify_token
from usecases.workout import add_workout_history, add_landmark_visit


class WorkoutService:
    @staticmethod
    async def workout_test(workout_request):
        # uid = verify_token(workout_request.token)
        uid = "test"
        cource_id = workout_request.course_id
        geometry_track = workout_request.move_history
        time = workout_request.total_time
        route = workout_request.route
        add_workout_history(uid, cource_id, geometry_track, time)
        return geometry_track
