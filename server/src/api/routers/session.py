from depends.auth import FirebaseToken
from fastapi import APIRouter, Depends
from routers.sessions import course, landmark, workout

router = APIRouter()

router.include_router(
    workout.router,
    prefix="/workout",
)

router.include_router(
    landmark.router,
    prefix="/landmark",
)

router.include_router(
    course.router,
    prefix="/course",
)


@router.get("/")
async def get_session(fbToken: FirebaseToken = Depends()):
    return "logged in user"
