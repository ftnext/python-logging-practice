# /// script
# dependencies = ["httpx", "rich"]
# ///

import logging.config

import httpx
from rich.pretty import pprint

# equivalent https://rednafi.com/python/no_hijack_root_logger/
logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "console": {
                "format": "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
            }
        },
        "loggers": {
            "httpx": {
                "level": "DEBUG",
                "handlers": ["console"],
            }
        },
    }
)

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
