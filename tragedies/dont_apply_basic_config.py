import logging

import antipattern_logging.call_basic_config  # Call basicConfig once

# ref: https://github.com/python/cpython/blob/v3.12.5/Lib/logging/__init__.py#L2097-L2099
# root_logger = logging.getLogger()
# for handler in root_logger.handlers[:]:
#     root_logger.removeHandler(handler)
#     handler.close()
# >This function does nothing if the root logger already has handlers configured
# https://docs.python.org/3/library/logging.html#logging.basicConfig
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
)
# root_logger.info("INFO log")  # Not printed

# By library, level=INFO, format=%(levelname)s:%(name)s:%(message)s
logging.getLogger().warning("ちょっとヤバいよ")
