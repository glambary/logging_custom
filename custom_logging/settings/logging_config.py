import sys

import structlog

from custom_logging.base.formatter import log_formatter_custom
from custom_logging.settings.schemas import LevelType


def get_logging_config(
        path_to_warning_logs: str,
        project_name: str,
        log_level: LevelType
):
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console_formatter": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processors": [
                    structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                    log_formatter_custom,
                ],
            },
            "console_formatter_for_other_logs": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processors": [
                    structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                    structlog.processors.TimeStamper(fmt="iso"),
                    structlog.stdlib.add_log_level,
                    log_formatter_custom,
                ],
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "console_formatter",
                "stream": sys.stdout,
            },
            "console_for_other_logs": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "console_formatter_for_other_logs",
                "stream": sys.stdout,
            },
            "file": {
                "level": "WARNING",
                "class": "logging.FileHandler",
                "formatter": "console_formatter",
                "filename": path_to_warning_logs,
            },
        },
        "loggers": {
            "fastapi_sdk": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,  # если False, то после обработки лога,
                # не передаёт его последующим логгерам
            },
            project_name: {
                "handlers": ["console", "file"],
                "level": log_level.value,
                "propagate": False,  # если False, то после обработки лога,
                # не передаёт его последующим логгерам
            },
            "": {
                "handlers": ["console_for_other_logs"],
                "level": log_level.value,
            },
        },
    }
