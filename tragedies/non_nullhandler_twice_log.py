import logging

from antipattern_logging.add_non_nullhandler import awesome

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)

awesome()
