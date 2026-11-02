import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

def _get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if not database_url or database_url.startswith(("http://", "https://")):
        return "sqlite:///./employee_management.db"
    return database_url


engine = create_engine(_get_database_url(), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()