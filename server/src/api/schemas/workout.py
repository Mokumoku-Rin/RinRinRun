from pydantic import BaseModel
from typing import List


class WorkoutRequest(BaseModel):
    properties: WorkoutProperties
    landmark_visits: List[WorkoutLandmarkVisit] = []
    geo_json: WorkoutGeoJson


class WorkoutProperties(BaseModel):
    time_list: list
    total_distance: int
    total_time: int

class WorkoutLandmarkVisit(BaseModel):
    id: int
    time: int

class WorkoutGeoJson(BaseModel):
    type: str
    coordinates: List[List[float]]


class WorkoutResponse(BaseModel):
    result: str
