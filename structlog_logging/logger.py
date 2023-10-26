import structlog


class Logger:
    def __init__(self, project_name: str):
        self.project_name = project_name

    def get_logger(self, name: str = __name__):
        return structlog.get_logger(
            self.project_name, project=self.project_name, logger_=name
        )
