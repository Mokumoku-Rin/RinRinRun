from depends.auth import FirebaseToken
from fastapi import APIRouter, Depends
from schemas.workout import (WorkoutBasedOnDateResponse, WorkoutRequest,
                             WorkoutResponse)
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
