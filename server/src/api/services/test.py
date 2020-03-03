from schemas.test import TestSchema

class TestService:
  @staticmethod
  def create_test_response(req: TestSchema):
    print(req)
    return {"result": "received"}
