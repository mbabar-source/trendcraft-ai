from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite file in the project folder (created on first run)
SQLALCHEMY_DATABASE_URL = "sqlite:///./trendcraft.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Open a DB session for a request; close it when the request ends."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
