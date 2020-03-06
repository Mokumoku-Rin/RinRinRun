from pydantic import BaseModel


class ImageResponse(BaseModel):
    result: str


class ImageRequest(BaseModel):
    landmark_id: int
    course_id: int
    img: str
