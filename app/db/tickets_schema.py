import enum
import uuid
from datetime import UTC, datetime
from enum import Enum, IntEnum, StrEnum, auto

import sqlalchemy
from sqlalchemy import DateTime, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from app.core.config import config

engine = create_engine(config.db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Status(StrEnum):
    OPEN = auto()
    STALLED = auto()
    CLOSED = auto()


class Base(DeclarativeBase):
    pass


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[uuid.UUID] = mapped_column(
        sqlalchemy.UUID, primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(default=str)
    status: Mapped[Status] = mapped_column(default=Status.OPEN)
    created_at: Mapped[datetime] = mapped_column(default=lambda _: datetime.now(UTC))
