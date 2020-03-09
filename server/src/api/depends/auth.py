import os
from random import randint
from fastapi import Header, HTTPException, Response
from firebase_admin import auth, exceptions

from usecases.auth import verify_token

class FirebaseToken:
  def __init__(self, x_token: str = Header(...)):
    if x_token == None:
      raise HTTPException(403, detail="X-Token verification error: not logged in")

    # on development, skip token verification
    if os.environ["SERVER_ENV"] == "development":
      if x_token == "1":
        self.uid = 1
      elif x_token == "2":
        self.uid = 2
      else:
        self.uid = "development_" + str(randint(0,1000000))
      return

    self.uid = verify_token(x_token)
