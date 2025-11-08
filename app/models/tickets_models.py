import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from app.db.tickets_schema import Status


class TicketCreate(BaseModel):
    title: str
    description: str | None = None


class TicketRead(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None = None
    status: Status
    created_at: datetime

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%SZ")
