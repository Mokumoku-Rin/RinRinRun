from pydantic import BaseModel
from typing import List


class Property(BaseModel):
    time_list: str
    total_distance: int
    total_time: int
    course_id: int


class VisitLandmark(BaseModel):
    id: int
    time: int


class WorkoutRequest(BaseModel):
    properties: Property
    landmark_visits: List[VisitLandmark]
    geo_json: str


class WorkoutResponse(BaseModel):
    result: str
