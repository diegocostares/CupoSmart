import time

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException

from ia import get_all_available_courses, get_best_order
from schemas import Course
from utils import logger_config

logger = logger_config(__name__)
load_dotenv()
api_router = APIRouter()


@api_router.get("/status")
async def read_hello():
    return {"status": "OK"}


@api_router.post("/courses", tags=["Courses"], response_model=Course)
async def create_courses(course: Course):
    """
    Este endpoint recibe una lista de 5 códigos de cursos y los retorna en un orden nuevo.
    """
    logger.debug(f"Se recibieron los cursos: {course.courses}")
    if len(course.courses) != 5:
        raise HTTPException(
            status_code=400, detail="Se requieren exactamente 5 códigos de curso"
        )
    course = get_best_order(course.courses, course.banner)
    return course


@api_router.get("/courses", tags=["Courses"])
async def get_courses():
    """
    Este endpoint retorna la lista de cursos disponibles.
    """
    logger.debug("Se recibió la solicitud de cursos disponibles")
    list_courses = get_all_available_courses()
    return {"courses": list_courses}
