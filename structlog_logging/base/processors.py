import logging
from typing import NoReturn

import structlog
from structlog.typing import EventDict

from core.settings import log_level


def filter_by_level_custom(
    _: logging.Logger, name: str, event_dict: EventDict
) -> EventDict | NoReturn:
    this_level: int = structlog.stdlib._NAME_TO_LEVEL[name]
    set_level: int = structlog.stdlib._NAME_TO_LEVEL[log_level.name]

    if this_level >= set_level:
        return event_dict

    raise structlog.DropEvent


def add_kwargs_in_event(
    _: logging.Logger, __: str, event_dict: EventDict
) -> EventDict:
    message = event_dict.pop("event", None)

    new_event_dict: EventDict = {"event": {}}

    if logger := event_dict.pop("logger_", False):
        new_event_dict["logger"] = logger

    if project := event_dict.pop("project", False):
        new_event_dict["project"] = project

    event: dict = new_event_dict["event"]

    if message:
        event["message"] = message

    event.update(event_dict)

    return new_event_dict
