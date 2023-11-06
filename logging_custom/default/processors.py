import structlog

from logging_custom.common.processors import (
    # filter_by_level_custom,
    add_kwargs_in_event
)

processors = [
    # filter_by_level_custom,
    add_kwargs_in_event,
    structlog.stdlib.add_log_level,
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.CallsiteParameterAdder(
        {
            structlog.processors.CallsiteParameter.FUNC_NAME,
            structlog.processors.CallsiteParameter.LINENO,
            structlog.processors.CallsiteParameter.PATHNAME,
            structlog.processors.CallsiteParameter.MODULE,
        }
    ),
    structlog.processors.UnicodeDecoder(),
    structlog.processors.ExceptionPrettyPrinter(),
    structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
]
