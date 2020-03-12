from depends.auth import FirebaseToken
from fastapi import APIRouter, Depends
from schemas.course import CourseGetAllResponse, CourseGetResponse
from services.course import CourseService

router = APIRouter()


@router.get("/", response_model=CourseGetAllResponse)
def get_course(sort_by: str = "popular", limit: int = 10):
    course_list = CourseService.get_course_list(sort_by, limit)
    response = {
        "courses": course_list
    }
    return response


@router.get("/{course_id}/", response_model=CourseGetResponse)
def get_course(course_id: int):
    course, landmarks = CourseService.gether_course_info(course_id)
    response = course
    response["landmarks"] = landmarks
    return response


@router.get("/{course_id}/ghost", response_model=None)
def get_course_ghost(course_id: int, fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    ghost_list = CourseService.gether_ghost_info_list(uid, course_id)
    response = {
        "ghosts": ghost_list
    }

    return response
