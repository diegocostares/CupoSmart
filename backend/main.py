import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from routes import api_router
from utils import logger_config

logger = logger_config("main")
logger.info("Starting the application.")

# REST API Settings
app = FastAPI(
    title="CupoSmart",
    description="API REST para la aplicación CupoSmart.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/", status_code=status.HTTP_204_NO_CONTENT)
async def root():
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
