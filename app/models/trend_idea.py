from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database import Base


class TrendIdea(Base):
    """AI-generated trend and content ideas (saved after /generate-ideas in a later step)."""

    __tablename__ = "trend_ideas"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(255), nullable=False)
    trend = Column(Text, nullable=False)
    category = Column(String(100), nullable=True)
    linkedin_post_idea = Column(Text, nullable=True)
    youtube_video_idea = Column(Text, nullable=True)
    blog_article_idea = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
