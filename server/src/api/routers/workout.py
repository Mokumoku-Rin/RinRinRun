from fastapi import APIRouter
from schemas.workout import WorkoutRequest, WorkoutResponse
from services.workout import WorkoutService

router = APIRouter()


@router.post("/", response_model=WorkoutResponse)
async def post_workout(workout_request: WorkoutRequest):
    message = await WorkoutService.workout_test(workout_request)
    response: WorkoutResponse = {
        "result": message
    }
    return response
