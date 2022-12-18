import logging

from .settings import Settings, _settings


def _configure_logger(logger: logging.Logger, settings: Settings) -> None:
    if settings.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    formatter = logging.Formatter(
        fmt="[%(levelname)-8s] [%(asctime)s]: %(message)s (%(filename)s)",
        datefmt="%d-%m %H:%M:%S",
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)


def get_logger(settings: Settings) -> logging.Logger:
    logger = logging.getLogger(__name__)
    _configure_logger(logger=logger, settings=settings)
    
    return logger


logger = get_logger(settings=_settings)
