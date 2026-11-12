from datetime import datetime

from pydantic import BaseModel,ConfigDict


class BookMark(BaseModel):
    url: str
    title: str
    description: str | None = None
    tags: list[str] | None = None

class BookMarkCreate(BookMark):
    pass

class BookMarkUpdate(BaseModel):
    url: str | None = None
    title: str | None = None
    description: str | None = None
    tags: list[str] | None = None

class BookMarkPublic(BaseModel):
    id: int
    url: str
    title: str
    description: str | None = None
    tags: list[str] | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
