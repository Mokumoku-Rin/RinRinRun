from typing import List

from pydantic import BaseModel


class LandmarkVisitResponse(BaseModel):
    result: str


class LandmarkVisitRequest(BaseModel):
    landmark_id: int
    course_id: int
    img: str


class LandmarkInfo(BaseModel):
    id: int
    name: str
    pos: str
    img_url: str
    description: str

class LandmarkResponse(BaseModel):
    landmarks: List[LandmarkInfo]

class LandmarkPostResponse(BaseModel):
    result: str


class LandmarkPostRequest(BaseModel):
    name: str
    description: str
    img_url: str
    pos: str
