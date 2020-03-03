from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_session():
  return "logged in"