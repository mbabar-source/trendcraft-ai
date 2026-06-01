from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SourceCreate(BaseModel):
    """What the client sends when creating a Source."""

    title: str | None = None
    body: str
    source_url: str | None = None
    platform: str | None = None


class SourceRead(BaseModel):
    """What the API returns for a Source."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    body: str
    source_url: str | None
    platform: str | None
    created_at: datetime

