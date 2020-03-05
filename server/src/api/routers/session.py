from fastapi import APIRouter, Depends
from depends.auth import FirebaseToken
from routers.sessions import workout

router = APIRouter()

router.include_router(
  workout.router,
  prefix="/workout",
)

@router.get("/")
async def get_session(fbToken: FirebaseToken = Depends()):
  return "logged in user"