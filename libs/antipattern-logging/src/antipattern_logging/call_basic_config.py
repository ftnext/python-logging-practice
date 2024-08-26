import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s"
)
logging.getLogger().info("想定通り")
