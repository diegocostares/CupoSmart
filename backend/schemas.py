"""
Archivo de esquemas de las request de Fast Api
"""
from typing import List, Optional

from pydantic import BaseModel, validator


class Course(BaseModel):
    courses: List[str]  # list of courses
    banner: int  # banner
