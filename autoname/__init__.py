__all__ = ['AutoName', "AutoNameLowercase", "AutoNameUppercase", 'auto']

from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class AutoNameLowercase(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

class AutoNameUppercase(Enum):
    def _generate_next_value_(name: str, start, count, last_values):
        return name.upper()