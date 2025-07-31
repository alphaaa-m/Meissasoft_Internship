from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator

DATABASE_URL = "sqlite:///./std_tchr.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
LocalSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = LocalSession() 
    try:
        yield db
    finally:
        db.close()