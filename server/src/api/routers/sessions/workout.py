from fastapi import APIRouter, Depends
from schemas.workout import WorkoutRequest, WorkoutResponse
from schemas.workout import Created_Workout_Response
from services.workout import WorkoutService
from depends.auth import FirebaseToken

router = APIRouter()


@router.post("/", response_model=WorkoutResponse)
async def post_workout(workout_request: WorkoutRequest, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    message = await WorkoutService.add_record(workout_request, uid)
    response: WorkoutResponse = {
        "result": message
    }
    return response


@router.get("/", response_model=Created_Workout_Response)
async def get_workout_history_based_date(date: str,
                                         fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    date = date
    response: Created_Workout_Response = {
        "date": date,
        "datas": await WorkoutService.get_based_on_date(uid, date + '%')
    }
    # response: TodayRequest = TodayService.get_today_record(uid, date)
    return response
