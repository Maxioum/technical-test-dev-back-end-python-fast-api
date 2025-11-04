from fastapi import FastAPI

from app.api.v1 import tickets_controller
from app.core.config import config
from app.core.logging import setup_logging
from app.db.tickets_schema import Base, engine

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.app_name)


# Register routes
app.include_router(tickets_controller.router, prefix="/api/v1")
