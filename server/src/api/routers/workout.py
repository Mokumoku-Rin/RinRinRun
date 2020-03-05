from fastapi import APIRouter
from schemas.workout import WorkoutRequest, WorkoutResponse

router = APIRouter()


@router.post("/", response_model=WorkoutResponse)
async def post_workout(workout_request: WorkoutRequest):
    message = "workout test"
    response: WorkoutResponse = {
        "result": message
    }
    return response
