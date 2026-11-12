from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models import BookMark
from app.routers import bookmarks


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan, title="Bookmarks API")

app.include_router(bookmarks.router)

@app.get("/health-check")
def check_health():
    return {"status": "ok"}