# /// script
# dependencies = ["httpx", "rich"]
# ///

# https://gist.github.com/ftnext/70cca003272a626bea11396e41b342e0
import logging

import httpx
from rich.pretty import pprint

# ref: https://rednafi.com/python/no_hijack_root_logger/
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
    "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(console_formatter)
httpx_logger.addHandler(console_handler)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
