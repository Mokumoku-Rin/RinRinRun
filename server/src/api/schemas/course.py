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
    shortest_time: int
    shortest_distance: int
    landmarks: List[LandmarkInfo]
