from schemas.test import TestSchema
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

class TestService:
  @staticmethod
  def create_test_response(req: TestSchema):
    print('Req:', req)
    default_app = firebase_admin.initialize_app()
    decoded_token = auth.verify_id_token(req.token)
    uid = decoded_token['uid']
    print('uid:', uid)
    return {"result": "received"}
