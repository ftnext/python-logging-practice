import logging

libA_logger = logging.getLogger("libA")
libB_logger = logging.getLogger("libB")


def libA_awesome():
    libA_logger.debug("awesome")


def libB_fabulous():
    libB_logger.debug("fabulous")


def main():
    libA_awesome()
    libB_fabulous()


if __name__ == "__main__":
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
        )
    )
    stream_handler.addFilter(logging.Filter("libA"))
    stream_handler.addFilter(logging.Filter("libB"))
    root_logger.addHandler(stream_handler)

    main()
