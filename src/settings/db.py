"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings.config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.postgres_user}:{settings.postgres_password}@"
    f"{settings.database_host}:{settings.pgport}/{settings.postgres_db}"
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"options": f"-csearch_path={settings.postgres_db_schema}"},
    echo=False,
    pool_size=50,
    max_overflow=0,
    pool_recycle=1800,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Get database connection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
