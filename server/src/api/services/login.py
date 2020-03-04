from firebase_admin import auth, exceptions
from fastapi import HTTPException

from usecases.auth import verify_token
from db.user import get_user, register_user


class LoginService:
    @staticmethod
    async def register(token: str):
      uid = verify_token(token)
      if get_user(uid):
        return "login"
      register_user(uid)
      return "created"
