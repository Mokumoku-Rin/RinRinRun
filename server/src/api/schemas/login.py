from pydantic import BaseModel

class LoginRequest(BaseModel):
  token: str
  img_url: str
  name: str

class LoginResponse(BaseModel):
  result: str