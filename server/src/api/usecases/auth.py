import os

from firebase_admin import auth, exceptions
from fastapi import HTTPException, status
from random import randint

def verify_token(token: str):
  # development
  if os.environ["SERVER_ENV"] == "development":
    return "development_" + str(randint(0,1000000))

  try:
    dec_token = auth.verify_id_token(token)
    return dec_token["uid"]
  except exceptions.FirebaseError as e:
    print(e)
    raise HTTPException(status.HTTP_403_FORBIDDEN, "X-Token verification error: " + str(e))
