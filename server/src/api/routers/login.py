from fastapi import APIRouter

router = APIRouter()

@router.get("/login/")
async def get_login():
  return {"page": "login"}