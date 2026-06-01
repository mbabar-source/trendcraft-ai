from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Source, TrendIdea  # noqa: F401 — register tables with Base
from app.schemas.source import SourceCreate, SourceRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "TrendCraftAI backend is running"}


@app.post("/sources", response_model=SourceRead, status_code=status.HTTP_201_CREATED)
def create_source(source_in: SourceCreate, db: Session = Depends(get_db)):
    source = Source(
        title=source_in.title,
        body=source_in.body,
        source_url=source_in.source_url,
        platform=source_in.platform,
    )

    db.add(source)
    db.commit()
    db.refresh(source)
    return source


@app.get("/sources", response_model=list[SourceRead])
def list_sources(db: Session = Depends(get_db)):
    return db.query(Source).order_by(Source.id.desc()).all()


@app.get("/sources/{source_id}", response_model=SourceRead)
def get_source(source_id: int, db: Session = Depends(get_db)):
    source = db.query(Source).filter(Source.id == source_id).first()
    if source is None:
        raise HTTPException(status_code=404, detail="Source not found")
    return source