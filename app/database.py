from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

sqlite_file = "database.db"
sqlite_url = f"sqlite:///{sqlite_file}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

