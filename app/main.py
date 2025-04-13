from app.models import Base
from app.database import engine
from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(
    title="Device Statistics Service",
    description="Service for collecting and analyzing device statistics.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")
Base.metadata.create_all(bind=engine)
