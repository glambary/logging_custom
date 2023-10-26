import structlog


def configure_structlog(processors: list):
    structlog.reset_defaults()

    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,  # type: ignore
        cache_logger_on_first_use=True,
    )
