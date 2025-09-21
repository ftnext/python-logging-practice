import logging
import sys

# from pythonjsonlogger.json import JsonFormatter
from rich.logging import RichHandler

from awesomelib import awesome

if len(sys.argv) > 1 and sys.argv[1] == "-v":
    log_level = logging.DEBUG
else:
    log_level = logging.WARNING

rich_handler = RichHandler()
# rich_handler.setFormatter(
#     JsonFormatter("%(name)s:%(funcName)s - %(message)s", json_ensure_ascii=False)
# )
logging.basicConfig(
    level=log_level,
    format="%(name)s:%(funcName)s - %(message)s",
    handlers=[rich_handler],
)

awesome()
