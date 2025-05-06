# app/utils/logger.py

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger with the specified name.

    :param name: Logger name (usually __name__)
    :return: Configured logger instance
    """
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # Avoid adding handlers multiple times

    logger.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    return logger
