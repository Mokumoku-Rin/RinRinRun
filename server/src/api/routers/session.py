from fastapi import APIRouter, Depends
from depends.auth import FirebaseToken
from routers.sessions import workout, landmark

router = APIRouter()

router.include_router(
    workout.router,
    prefix="/workout",
)

router.include_router(
    landmark.router,
    prefix="/landmark",
)


@router.get("/")
async def get_session(fbToken: FirebaseToken = Depends()):
    return "logged in user"
