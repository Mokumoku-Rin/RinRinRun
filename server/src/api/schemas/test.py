from pydantic import BaseModel


class TestSchema(BaseModel):
    token: str
    name: str
