from fastapi import FastAPI
from app.api import index
from app.config import settings
from app.config.logging import init_logging


# instantiate FastAPI app
app = FastAPI(title=settings.app_title)

# tasks to execute on startup
def startup():
    init_logging()

# include index router
app.include_router(index.router, prefix="/api")
app.add_event_handler("startup", startup)
