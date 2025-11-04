import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

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
