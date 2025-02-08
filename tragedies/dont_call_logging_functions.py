import logging

import antipattern_logging.call_root_logging  # Call basicConfig once

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)

logging.getLogger().info("INFO log")  # Not printed
