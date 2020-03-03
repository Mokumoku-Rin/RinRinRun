from schemas.test import TestSchema
from firebase_admin import auth

class TestService:
  @staticmethod
  def create_test_response(req: TestSchema):
    print('Req:', req)
    decoded_token = auth.verify_id_token(req.token)
    uid = decoded_token['uid']
    print('uid:', uid)
    return {"result": "received"}
