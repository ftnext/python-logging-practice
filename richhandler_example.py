import logging
import sys

from rich.logging import RichHandler

from awesomelib import awesome

if len(sys.argv) > 1 and sys.argv[1] == "-v":
    log_level = logging.DEBUG
else:
    log_level = logging.WARNING

logging.basicConfig(
    level=log_level,
    format="%(name)s:%(funcName)s - %(message)s",
    handlers=[RichHandler()],
)

awesome()
