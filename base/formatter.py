import logging

from structlog.typing import EventDict

from base.color import add_color_level, get_fore_color, \
    get_reset_all_colors


def log_formatter_custom(
    _: logging.Logger, __: str, event_dict: EventDict
) -> str:
    """
    Пример лога:
        INFO | 1993-07-03T15:00:00.000000Z |
        EVENT: {
            'message': 'Main function called',
            'kwarg1': ..., 'kwarg2': ..., ...
            } |
        PROJECT: ${PROJECT_NAME} |
        LOGGER: src.main |
        PATH: [main - 20 - setup], [/project/src/main.py]
        OTHER: ...

    в PATH [main - 20 - setup] = [file_name - line_number - function_name]
    """
    log = []

    if level := event_dict.pop("level", False):
        log.append(
            add_color_level(level.upper())
        )

    if timestamp := event_dict.pop("timestamp", False):
        log.append(timestamp)

    flag = event_dict.get('project')

    if flag:
        log[-1] += get_fore_color("MAGENTA")
        # log.append(get_fore_color("MAGENTA"))

    for key in ("event", "project", "logger"):
        if value := event_dict.pop(key, False):
            log.append(f"{key.upper()}: {value}")

    path = []

    if (
        (module := event_dict.pop("module", False))
        and (line_number := event_dict.pop("lineno", False))
        and (func_name := event_dict.pop("func_name", False))
    ):
        path.append(f"[{module} - {line_number} - {func_name}]")

    if pathname := event_dict.pop("pathname", False):
        path.append(f"[{pathname}]")

    if flag:
        log[-1] += get_fore_color("CYAN")
        # log.append(get_fore_color("CYAN"))

    if path:
        log.append(f"PATH: {', '.join(path)}")

    if event_dict:
        log.append(f"OTHER: {event_dict}")

    if flag:
        log[-1] += get_reset_all_colors()
        # log.append(get_reset_all_colors())

    return " | ".join(log)
