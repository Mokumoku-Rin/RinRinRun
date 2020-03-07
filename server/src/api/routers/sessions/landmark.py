from fastapi import APIRouter, Depends
from schemas.landmark import LandmarkVisitRequest, LandmarkVisitResponse
from services.landmark import LandmarkService
from depends.auth import FirebaseToken

router = APIRouter()


@router.post("/visit", response_model=LandmarkVisitResponse)
async def compare_image(landmark_request: LandmarkVisitRequest, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    message = await LandmarkService.ImageCompare(landmark_request)
    response: WorkoutResponse = {
        "result": message
    }
    return response
