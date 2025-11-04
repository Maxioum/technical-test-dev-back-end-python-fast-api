from typing import Generator

from pytest import fixture
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.db.tickets_schema import Base, Ticket
from app.services.tickets_service import TicketsService

# Setup the in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"


@fixture
def tickets_service() -> Generator[TicketsService]:
    engine = create_engine(
        DATABASE_URL,
        connect_args={
            "check_same_thread": False,
        },
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    yield TicketsService(session=session)

    session.close()
    engine.dispose()


@fixture
def ticket(tickets_service: TicketsService) -> Ticket:
    title = "Title"
    description = "description"
    return tickets_service.create_ticket(title=title, description=description)
