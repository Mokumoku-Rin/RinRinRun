from usecases.auth import verify_token
from usecases.workout import add_workout_history, add_landmark_visit, update_user_totaltime


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
