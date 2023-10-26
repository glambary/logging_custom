import logging.config

import structlog

from settings.structlog_config import configure_structlog


class Logger:
    def __init__(self, project_name: str):
        self.project_name = project_name

    def get_logger(self, name: str = __name__):
        return structlog.get_logger(
            self.project_name, project=self.project_name, logger_=name
        )

    @staticmethod
    def set_config(self, dict_config: dict, processors: list):
        """Подготовит struct logging к работе."""
        configure_structlog(processors)
        logging.config.dictConfig(dict_config)
