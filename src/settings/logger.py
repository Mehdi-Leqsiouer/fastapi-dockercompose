"""
Logging module.
get_app_logger returns a logging.Logger object with the given name.
"""

import logging


def get_app_logger(app_name="demo_fastapi") -> logging.Logger:
    """Create and configure logger.
    Arguments
    ---------
    app_name (str): Name of the app.

    Returns
    -------
    logger (logging.Logger): Logger object.
    """
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


DEFAULT_LOGGER = get_app_logger()
