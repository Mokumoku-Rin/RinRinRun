from pydantic import BaseModel


class LandmarkVisitResponse(BaseModel):
    result: str


class LandmarkVisitRequest(BaseModel):
    landmark_id: int
    course_id: int
    img: str
