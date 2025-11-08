import uuid

from fastapi import APIRouter, Depends, HTTPException

from app.db.tickets_schema import SessionLocal, Ticket
from app.models.tickets_models import TicketCreate, TicketRead
from app.services.tickets_service import TicketsService

router = APIRouter()


def get_ticket_service() -> TicketsService:
    return TicketsService(session=SessionLocal())


@router.post("/tickets", response_model=TicketRead)
def create_ticket(
    ticket_create: TicketCreate, service: TicketsService = Depends(get_ticket_service)
) -> Ticket:
    return service.create_ticket(ticket_create.title, ticket_create.description)


@router.get("/tickets", response_model=list[TicketRead])
def get_all_tickets(service: TicketsService = Depends(get_ticket_service)) -> Ticket:
    tickets = service.get_all_tickets()
    return tickets


@router.get("/tickets/{ticket_id}", response_model=TicketRead)
def get_ticket(
    ticket_id: uuid.UUID, service: TicketsService = Depends(get_ticket_service)
) -> Ticket:
    ticket = service.get_ticket(ticket_id)
    return ticket


@router.patch("/tickets/{ticket_id}/close", response_model=TicketRead)
def close_ticket(
    ticket_id: uuid.UUID, service: TicketsService = Depends(get_ticket_service)
) -> Ticket | None:
    ticket = service.close_ticket(ticket_id)

    return ticket


@router.put("/tickets/{ticket_id}", response_model=TicketRead)
def modify_ticket(
    ticket_id: uuid.UUID,
    ticket_modify: TicketCreate,
    service: TicketsService = Depends(get_ticket_service),
) -> Ticket | None:
    ticket = service.modify_ticket(
        ticket_id, ticket_modify.title, ticket_modify.description
    )

    return ticket
