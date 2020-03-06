from fastapi import APIRouter, Depends
from depends.auth import FirebaseToken
from routers.sessions import workout, image

router = APIRouter()

router.include_router(
    workout.router,
    prefix="/workout",
)

router.include_router(
    image.router,
    prefix="/image",
)


@router.get("/")
async def get_session(fbToken: FirebaseToken = Depends()):
    return "logged in user"
