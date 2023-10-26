import logging.config
from typing import Optional

import structlog

from structlog_logging.settings.schemas import LevelType
from structlog_logging.settings.structlog_config import configure_structlog


class Logger:
    def __init__(
            self,
            project_name: str, level_type: LevelType, path_to_warning_logs: str
    ):
        self.project_name = project_name
        self.level_type = level_type
        self.path_to_warning_logs = path_to_warning_logs

    def get_logger(self, name: str = __name__):
        return structlog.get_logger(
            self.project_name, project=self.project_name, logger_=name
        )

    def set_config(
            self,
            logger_dict_config: Optional[dict] = None,
            processors: Optional[list] = None
    ):
        if logger_dict_config is None:
            from structlog_logging.settings.logging_config import \
                get_logging_config
            logger_dict_config = get_logging_config(
                self.path_to_warning_logs,
                self.project_name,
                self.level_type
            )

        if processors is None:
            from structlog_logging.settings.base_processors import \
                base_processors
            processors = base_processors
        configure_structlog(processors)
        logging.config.dictConfig(logger_dict_config)
