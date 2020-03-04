from fastapi import Header, HTTPException, Response
from firebase_admin import auth, exceptions

from usecases.auth import verify_token

async def verify_firebase_token(x_token: str = Header(...)):
  if x_token == None:
    raise HTTPException(403, detail="X-Token verification error: not logged in")
  uid = verify_token(x_token)
