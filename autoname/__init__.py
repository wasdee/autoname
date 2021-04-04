__all__ = ['AutoName', "AutoNameLowercase", "AutoNameUppercase", 'auto']

import re
from enum import Enum, auto



class AutoName(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class AutoNameLowercase(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class AutoNameUppercase(str, Enum):
    def _generate_next_value_(name: str, start, count, last_values):
        return name.upper()

# From https://github.com/dmontagu/fastapi-utils/blob/af95ff4a8195caaa9edaa3dbd5b6eeb09691d9c7/fastapi_utils/camelcase.py#L4
def snake2camel(snake: str, start_lower: bool = False) -> str:
    """
    Converts a snake_case string to camelCase.
    The `start_lower` argument determines whether the first letter in the generated camelcase should
    be lowercase (if `start_lower` is True), or capitalized (if `start_lower` is False).
    """
    camel = snake.title()
    camel = re.sub("([0-9A-Za-z])_(?=[0-9A-Z])", lambda m: m.group(1), camel)
    if start_lower:
        camel = re.sub("(^_*[A-Z])", lambda m: m.group(1).lower(), camel)
    return camel

class AutoNameCamelcase(str, Enum):
    """
    CamelStrEnum subclasses that create variants using `auto()` will have values equal to their camelCase names
    """

    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values) -> str:  # type: ignore
        """
        Uses the camelCase name as the automatic value, rather than an integer
        See https://docs.python.org/3/library/enum.html#using-automatic-values for reference
        """
        return snake2camel(name, start_lower=True)