import logging.config

import structlog


def configure_structlog(processors: list):
    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,  # type: ignore
        cache_logger_on_first_use=True,
    )


def set_config(dict_config: dict, processors: list):
    """Подготовит struct logging к работе."""
    structlog.reset_defaults()
    logging.shutdown()

    configure_structlog(processors)
    logging.config.dictConfig(dict_config)
