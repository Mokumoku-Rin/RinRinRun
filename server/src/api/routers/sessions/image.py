from fastapi import APIRouter, Depends
from schemas.image import ImageRequest, ImageResponse
from services.image import ImageService
from depends.auth import FirebaseToken

router = APIRouter()


@router.post("/compare", response_model=ImageResponse)
async def compare_image(image_request: ImageRequest, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    message = await ImageService.ImageCompare(image_request)
    response: WorkoutResponse = {
        "result": message
    }
    return response
