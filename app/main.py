from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models import Source, TrendIdea  # noqa: F401 — register tables with Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "TrendCraftAI backend is running"}