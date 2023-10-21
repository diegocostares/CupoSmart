import time

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException

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
    # TODO: Hacer un llamado a la funcion que ordena los cursos
    time.sleep(5)
    return course
