from fastapi import APIRouter
from schemas.login import LoginRequest, LoginResponse
from services.login import LoginService

router = APIRouter()


@router.get("/")
async def get_login():
    return "get login"


@router.post("/", response_model=LoginResponse)
async def post_login(loginRequest: LoginRequest):
    token = loginRequest.token
    name = loginRequest.name
    img_url = loginRequest.img_url
    message = await LoginService.register(token, name, img_url)
    response: LoginRequest = {
        "result": message
    }
    return response
