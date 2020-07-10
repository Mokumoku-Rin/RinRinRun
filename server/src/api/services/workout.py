from usecases.auth import verify_token
from usecases.workout import (add_landmark_visit, add_workout_history,
                              select_history_based_on_date,
                              update_course_status,
                              get_all_by_course_id)


class WorkoutService:
    @staticmethod
    async def add_record(workout_request, uid):
        time_list = workout_request.properties.time_list
        total_distance = workout_request.properties.total_distance
        total_time = workout_request.properties.total_time
        course_id = workout_request.properties.course_id

        landmark_visits = workout_request.landmark_visits
        geo_json = workout_request.geo_json

        insert_id = add_workout_history(uid, course_id, total_time,
                                        total_distance, time_list, geo_json)
        add_landmark_visit(uid, insert_id, landmark_visits)

        update_course_status(course_id, total_time, total_distance)

        return "OK"

    @staticmethod
    async def get_based_on_date(uid, date):
        return select_history_based_on_date(uid, date)

    @staticmethod
    async def get_results_by_course_id(cid):
        all_results = get_all_by_course_id(cid)
        uids = []
        for result in all_results:
            if result["user_id"] not in uids:
                uids.append(result["user_id"])
        
        best_results = []

        for uid in uids:
            user_results = []
            for r in all_results:
                if r["user_id"] == uid:
                    user_results.append(r)
            
            best = min(user_results, key=lambda r: r["total_time"])
            best_results.append({
                "total_time": int(best["total_time"]),
                "total_distance": int(best["total_distance"])
            })
        
        return best_results

        