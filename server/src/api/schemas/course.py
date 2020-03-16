from typing import List

from pydantic import BaseModel
from schemas.landmark import LandmarkInfo


class CourseSummary(BaseModel):
    id: int
    name: str
    description: str


class CourseGetAllResponse(BaseModel):
    courses: List[CourseSummary] = None


class CourseGetResponse(BaseModel):
    id: int
    name: str
    description: str
    mean_distance: int
    mean_time: int
    shortest_time: int = None
    shortest_distance: int = None
    landmarks: List[LandmarkInfo]


class CoursePostRequest(BaseModel):
    name: str
    description: str
    landmarks: List[int]


class CorsePostResponse(BaseModel):
    result: str
