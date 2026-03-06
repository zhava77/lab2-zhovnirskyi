"""Logging module for event processing."""

import logging

logger = logging.getLogger("event_processing")
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def log_event(event):
    """Log an event dispatch."""
    logger.info("Event dispatched: %s", event)


def log_error(message: str):
    """Log an error message."""
    logger.error(message)


def set_level(level: str):
    """Set logging level dynamically."""
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
    }
    logger.setLevel(levels.get(level.upper(), logging.INFO))
