from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_login():
  return "get login"