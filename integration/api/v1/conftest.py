from typing import Dict, Generator
from uuid import UUID, uuid4

from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.api.v1.tickets_controller import get_ticket_service
from app.db.tickets_schema import Base, Ticket
from app.main import app
from app.services.tickets_service import TicketsService

# Setup the in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"


@fixture()
def client() -> Generator[TestClient]:
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
    client_ = TestClient(app)

    def override_get_user_service() -> Generator[TicketsService]:
        # Setup the TestClient
        yield TicketsService(session=session)

    app.dependency_overrides[get_ticket_service] = override_get_user_service

    yield client_

    client_.close()


@fixture
def ticket(client: TestClient) -> Dict:
    response = client.post(
        "/api/v1/tickets", json={"title": "Title", "description": "description"}
    )
    return response.json()
