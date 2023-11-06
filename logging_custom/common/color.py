from typing import Literal

from colorama import Fore, Style

COLOR = Literal[
    "BLACK", "RED", "GREEN", "YELLOW",
    "BLUE", "MAGENTA", "CYAN", "WHITE",
    "RESET"
]

colors = {
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.RED + Style.BRIGHT,
}


def add_color_level(level: str) -> str:
    color = colors.get(level, Fore.WHITE)
    return f"{color}{level}{Style.RESET_ALL}"


def get_fore_color(color: COLOR) -> str:
    return getattr(Fore, color)


def get_reset_all_colors() -> str:
    return Style.RESET_ALL
