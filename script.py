import logging
import sys

from awesomelib import awesome

if len(sys.argv) > 1 and sys.argv[1] == "-v":
    log_level = logging.DEBUG
else:
    log_level = logging.WARNING

logging.basicConfig(
    level=log_level,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)

awesome()
