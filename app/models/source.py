from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database import Base


class Source(Base):
    """A Reddit or forum post we save for later analysis."""

    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    body = Column(Text, nullable=False)
    source_url = Column(String(500), nullable=True)
    platform = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
