from fastapi import APIRouter, Depends
from schemas.workout import WorkoutRequest, WorkoutResponse
from depends.auth import FirebaseToken

router = APIRouter()


@router.post("/", response_model=WorkoutResponse)
async def post_workout(workout_request: WorkoutRequest, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid

    message = "workout test"
    response: WorkoutResponse = {
        "result": message
    }
    return response
