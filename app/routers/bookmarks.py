import select

from fastapi import APIRouter, HTTPException

from app.dependencies import SessionDep
from app.models import BookMark
from app.schemas import BookMarkCreate, BookMarkPublic, BookMarkUpdate

router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"],
)

@router.post("/", response_model=BookMarkPublic, status_code=201)
def create_bookmark(session: SessionDep,bookmark: BookMarkCreate):
    bookmark_db = BookMark(**bookmark.model_dump())
    session.add(bookmark_db)
    session.commit()
    session.refresh(bookmark_db)
    return bookmark_db

@router.get("/",  response_model=list[BookMarkPublic])
def get_bookmarks(session: SessionDep):
    bookmarks_db = session.scalars(select(BookMark)).all()
    # TODO - ADD FILTERS

    if not bookmarks_db:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmarks_db

@router.get("/{id}", response_model=BookMarkPublic)
def get_bookmark(id: int, session: SessionDep):
    bookmark_db = session.get(BookMark, id)
    if not bookmark_db:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark_db

@router.patch("/{id}", response_model=BookMarkPublic)
def update_bookmark(id: int, bookmark: BookMarkUpdate, session: SessionDep):
    bookmark_db = session.get(BookMark, id)
    if not bookmark_db:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    update_data = bookmark.model_dump(exclude_unset=True)
    for f,v in update_data.items():
        setattr(bookmark_db, f, v)

    session.add(bookmark_db)
    session.commit()
    session.refresh(bookmark_db)
    return bookmark_db

@router.delete("/{id}", status_code=204)
def delete_bookmark(id: int, session: SessionDep):
    bookmark_db = session.get(BookMark, id)
    if not bookmark_db:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    session.delete(bookmark_db)
    session.commit()
    return None