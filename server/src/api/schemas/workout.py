from pydantic import BaseModel
from typing import List


class property(BaseModel):
    time_list: List[int]
    total_distance: int
    total_time: int
    course_id: int


class visit_landmark(BaseModel):
    id: int
    time: int


class WorkoutRequest(BaseModel):
    properties: property
    landmark_visits: List[visit_landmark]
    geo_json: str


class WorkoutResponse(BaseModel):
    result: str
