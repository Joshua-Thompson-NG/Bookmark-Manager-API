from datetime import datetime

from pydantic import BaseModel,ConfigDict, HttpUrl


class BookMark(BaseModel):
    url: HttpUrl
    title: str
    description: str | None = None
    tags: list[str] | None = None

class BookMarkCreate(BookMark):
    pass

class BookMarkUpdate(BaseModel):
    url: HttpUrl | None = None
    title: str | None = None
    description: str | None = None
    tags: list[str] | None = None

class BookMarkPublic(BaseModel):
    id: int
    url: HttpUrl
    title: str
    description: str | None = None
    tags: list[str] | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
