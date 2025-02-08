import logging
import logging.config
import sys


def init_logger() -> None:
    handler = logging.StreamHandler(stream=sys.stdout)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.info("Logger initated!")
