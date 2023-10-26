import logging.config

import structlog

from structlog_logging.settings.processors import base_processors


def configure_structlog(processors: list):
    structlog.reset_defaults()

    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,  # type: ignore
        cache_logger_on_first_use=True,
    )


def set_config(dict_config: dict, processors: list = base_processors):
    """Подготовит struct logging к работе."""
    configure_structlog(processors)
    logging.config.dictConfig(dict_config)
