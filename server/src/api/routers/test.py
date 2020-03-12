from fastapi import APIRouter
from schemas.test import TestSchema
from services.test import TestService

router = APIRouter()


@router.post("/")
async def post_test(body: TestSchema):
    reponse: object = TestService.create_test_response(body)
    return {"result": "received"}
