from firebase_admin import auth, exceptions
from fastapi import HTTPException, status

def verify_token(token: str):

  print("received token:" + token)

  try:
    dec_token = auth.verify_id_token(token)
    return dec_token["uid"]
  except exceptions.FirebaseError as e:
    print(e)
    raise HTTPException(status.HTTP_403_FORBIDDEN, "X-Token verification error: " + str(e))
