from firebase_admin import auth, exceptions
from fastapi import HTTPException

from usecases.auth import verify_token
from db.register import check_register

class LoginService:
  @staticmethod
  async def register(token: str):
    uid = verify_token(token)
    if check_register(uid):
      return "login"
    return "created"
    # or maybe "authenticated"
