from datetime import datetime
from typing import Dict

from fastapi.testclient import TestClient


def test_isoformat(client: TestClient, ticket: Dict) -> None:
    get_response = client.get(f"/api/v1/tickets/{ticket['id']}")

    created_at = get_response.json()["created_at"]
    assert "Z" in created_at
    assert datetime.fromisoformat(created_at)
