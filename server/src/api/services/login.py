from firebase_admin import auth, exceptions
from fastapi import HTTPException

from usecases.auth import verify_token

class LoginService:
  @staticmethod
  async def register(token: str):
    uid = verify_token(token)
    # todo db access to whether registered or not
    print(token)
    return "created"
    # or maybe "authenticated"
