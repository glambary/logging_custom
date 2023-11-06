from typing import Optional

import structlog

from logging_custom.common.schemas import LevelType
from logging_custom.settings import set_config


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
            logger_dict_config = self._get_default_dict_config()

        if processors is None:
            processors = self._get_default_processors()

        set_config(dict_config=logger_dict_config, processors=processors)

    def _get_default_dict_config(self):
        from logging_custom.default.logging_config import \
            get_logging_config

        return get_logging_config(
            self.path_to_warning_logs,
            self.project_name,
            self.level_type
        )

    @staticmethod
    def _get_default_processors():
        from logging_custom.default.processors import \
            processors

        return processors
