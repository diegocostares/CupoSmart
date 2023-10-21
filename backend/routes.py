from dotenv import load_dotenv
from fastapi import APIRouter

load_dotenv()
api_router = APIRouter()


@api_router.get("/hellow")
async def read_hello():
    return {"message": "Hola Mundo"}
