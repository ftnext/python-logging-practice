import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def awesome() -> None:
    logger.info("想定通り")
