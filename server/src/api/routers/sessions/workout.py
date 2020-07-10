from depends.auth import FirebaseToken
from fastapi import APIRouter, Depends, Path
from schemas.workout import (WorkoutBasedOnDateResponse, WorkoutRequest,
                             WorkoutResponse, WorkoutByCourseIdResponse)
from services.workout import WorkoutService

router = APIRouter()


@router.post("/", response_model=WorkoutResponse)
async def post_workout(workout_request: WorkoutRequest, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    message = await WorkoutService.add_record(workout_request, uid)
    response: WorkoutResponse = {
        "result": message
    }
    return response


@router.get("/", response_model=WorkoutBasedOnDateResponse)
async def get_workout_history_based_date(date: str,
                                         fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    date = date
    response: WorkoutBasedOnDateResponse = {
        "date": date,
        "datas": await WorkoutService.get_based_on_date(uid, date + '%')
    }
    # response: TodayRequest = TodayService.get_today_record(uid, date)
    return response


@router.get("/course/{course_id}", response_model=WorkoutByCourseIdResponse)
async def get_workout_by_course_id(
    course_id: int = Path(...,title="courseid for searching"),
    fbToken: FirebaseToken = Depends()
):
    response: WorkoutByCourseIdResponse = {
        "course_id": int(course_id),
        "results": await WorkoutService.get_results_by_course_id(course_id),
    }
    return response
