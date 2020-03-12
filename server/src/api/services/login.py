from fastapi import HTTPException
from firebase_admin import auth, exceptions
from usecases.auth import verify_token
from usecases.user import add_user, is_existed_user


class LoginService:
    @staticmethod
    async def register(token: str, name: str, img_url: str):
        uid = verify_token(token)
        if is_existed_user(uid):
            return "login"
        add_user(uid, name, img_url)
        return "created"
