from fastapi import APIRouter, Depends
from schemas.landmark import (
    LandmarkVisitRequest, LandmarkVisitResponse,
    LandmarkPostResponse, LandmarkPostRequest)
from services.landmark import LandmarkService
from depends.auth import FirebaseToken

router = APIRouter()


@router.post("/visit/", response_model=LandmarkVisitResponse)
async def compare_image(landmark_request: LandmarkVisitRequest, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    message = await LandmarkService.ImageCompare(landmark_request)
    response: WorkoutResponse = {
        "result": message
    }
    return response


@router.post("/", response_model=LandmarkPostResponse)
async def post_landmark(request_model: LandmarkPostRequest):
    name = request_model.name
    description = request_model.description
    img_url = request_model.img_url
    pos = request_model.pos
    message = await LandmarkService.post_landmark(name, description, img_url, pos)
    response: response_model = {
        "result": message
    }
    return response
