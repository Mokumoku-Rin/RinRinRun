from fastapi import Header, HTTPException, Response
from firebase_admin import auth, exceptions

async def verify_firebase_token(x_token: str = Header(...)):
  if x_token == None:
    raise HTTPException(403, detail="X-Token verification error: not logged in")
  
  try:
    dec_token = auth.verify_id_token(x_token)
  except exceptions.FirebaseError as e:
    raise HTTPException(e.code, "X-Token verification error: " + e.message)

  # and then authentication is OK
  Response.headers.append("X-Token", x_token)

