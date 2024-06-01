import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def awesome() -> None:
    logger.info("想定通り")
    logger.warning("ちょっとヤバいよ")
    print("Awesome ✨")
