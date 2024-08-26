import logging

import antipattern_logging.call_basic_config  # Call basicConfig once

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)

# By library, level=INFO, format=%(levelname)s:%(name)s:%(message)s
logging.getLogger().warning("ちょっとヤバいよ")
