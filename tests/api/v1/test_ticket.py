from uuid import UUID

import pytest

from app.db.tickets_schema import Status, Ticket
from app.services.tickets_service import TicketNotFoundError, TicketsService


def test_create_ticket(tickets_service: TicketsService) -> None:
    title = "Title"
    description = "description"

    ticket = tickets_service.create_ticket(title=title, description=description)

    assert ticket.title == title
    assert ticket.description == description


def test_get_ticket(tickets_service: TicketsService, ticket: Ticket) -> None:
    assert tickets_service.get_ticket(ticket.id) == ticket


def test_get_ticket_missing(
    tickets_service: TicketsService, non_existing_uuid: UUID
) -> None:
    with pytest.raises(TicketNotFoundError):
        tickets_service.get_ticket(non_existing_uuid)


def test_get_all_tickets(tickets_service: TicketsService, ticket: Ticket) -> None:
    assert tickets_service.get_all_tickets() == [ticket]


def test_modify_ticket(tickets_service: TicketsService, ticket: Ticket) -> None:
    new_description = "new_description"
    new_title = "new_title"

    new_ticket = tickets_service.modify_ticket(ticket.id, new_title, new_description)

    assert new_ticket
    assert new_ticket.title == new_title
    assert new_ticket.description == new_description


def test_modify_ticket_missing(
    tickets_service: TicketsService, non_existing_uuid: UUID
) -> None:
    new_description = "new_description"
    new_title = "new_title"

    with pytest.raises(TicketNotFoundError):
        tickets_service.modify_ticket(
            non_existing_uuid, title=new_title, description=new_description
        )


def test_close_ticket(tickets_service: TicketsService, ticket: Ticket) -> None:
    tickets_service.close_ticket(ticket.id)

    assert ticket.status == Status.CLOSED


def test_close_ticket_missing(
    tickets_service: TicketsService, non_existing_uuid: UUID
) -> None:
    with pytest.raises(TicketNotFoundError):
        tickets_service.close_ticket(non_existing_uuid)
