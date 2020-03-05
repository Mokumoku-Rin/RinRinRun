from pydantic import BaseModel
from typing import List


class Route(BaseModel):
    arrive_order: int
    landmark: str
    time: float


class WorkoutRequest(BaseModel):
    course_id: int
    move_history: str
    total_time: float
    route: List[Route]


class WorkoutResponse(BaseModel):
    result: str