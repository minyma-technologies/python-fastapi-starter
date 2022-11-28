import logging
from uvicorn.logging import DefaultFormatter
from app.config import settings


def init_logging():
    # create logger
    logger = logging.getLogger("default")
    logger.setLevel(settings.log_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.log_level)

    # add default formatter to handler
    FORMAT: str = "%(levelprefix)s %(asctime)s | %(message)s"
    ch.setFormatter(DefaultFormatter(FORMAT))

    # add ch to logger
    logger.addHandler(ch)
