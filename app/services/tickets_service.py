import uuid
from typing import Optional

from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import Session

from app.db.tickets_schema import Status, Ticket


class TicketNotFoundError(Exception):
    pass


class MultipleTicketsFoundError(Exception):
    pass


class TicketsService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def get_ticket(self, ticket_id: uuid.UUID) -> Ticket:
        """Get a ticket by its id."""

        try:
            ticket = self._db.query(Ticket).filter(Ticket.id == ticket_id).one()
        except NoResultFound as e:
            raise TicketNotFoundError(f"Ticket with id {ticket_id} not found") from e
        except MultipleResultsFound as e:
            raise MultipleTicketsFoundError(
                f"Multiple Tickets with id {ticket_id} found"
            ) from e

        return ticket

    def create_ticket(self, title: str, description: Optional[str] = None) -> Ticket:
        """Create a ticket with a title and an optional description."""

        ticket = Ticket(title=title, description=description or "")

        self._db.add(ticket)
        self._db.commit()
        self._db.refresh(ticket)

        return ticket

    def get_all_tickets(self) -> Ticket:
        """Get all the tickets"""
        tickets = self._db.query(Ticket).all()

        return tickets

    def modify_ticket(
        self,
        ticket_id: uuid.UUID,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Ticket | None:
        """Modify the title and/or the description of a ticket."""

        ticket = self.get_ticket(ticket_id)

        if not ticket:
            return None

        if title:
            ticket.title = title

        if description is not None:
            ticket.description = description

        self._db.commit()
        self._db.refresh(ticket)

        return ticket

    def close_ticket(self, ticket_id: uuid.UUID) -> Ticket | None:
        """Mark ticket as closed."""
        ticket = self.get_ticket(ticket_id)

        if ticket is None:
            return None

        ticket.status = Status.CLOSED

        self._db.commit()
        self._db.refresh(ticket)
        return ticket
