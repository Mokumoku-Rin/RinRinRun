from pydantic import BaseModel
from typing import List


class TodayRequest(BaseModel):
    date: str


class Data(BaseModel):
    total_distance: int
    total_time: int
    geo_json: dict


class TodayResponse(BaseModel):
    date: str
    datas: List[Data]
