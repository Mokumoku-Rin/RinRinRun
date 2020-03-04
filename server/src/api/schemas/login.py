from pydantic import BaseModel

class LoginRequest(BaseModel):
  token: str

class LoginResponse(BaseModel):
  result: str