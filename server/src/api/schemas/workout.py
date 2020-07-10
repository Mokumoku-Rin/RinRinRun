from typing import List

from pydantic import BaseModel


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


class Data(BaseModel):
    total_distance: int
    total_time: int
    geo_json: dict


class WorkoutBasedOnDateResponse(BaseModel):
    date: str
    datas: List[Data]

class WorkoutResult(BaseModel):
    total_time: int #ms
    total_distance: int # metre


class WorkoutByCourseIdResponse(BaseModel):
    course_id: str
    results: List[WorkoutResult]

