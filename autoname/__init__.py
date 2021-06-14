__all__ = ['AutoName', 'StrEnum', "AutoNameLower", "AutoNameUpper", "LowerStrEnum", "UpperStrEnum", "AutoNameSnake2Camel", 'snake2camel', 'transform', 'make_strEnum', ]

import inspect
import re
import uuid
from enum import Enum, auto
from typing import Type, Callable


class AutoName(str, Enum):
    """
    an enum `AutoName` from [python docs](https://docs.python.org/3/library/enum.html#using-automatic-values) with multiple stringcase options.
    """
    def _generate_next_value_(name, start, count, last_values):
        return name

StrEnum = AutoName

class AutoNameLower(AutoName):
    def _generate_next_value_(name, start, count, last_values):
        return str.lower(name)

LowerStrEnum = AutoNameLower

class AutoNameUpper(AutoName):
    def _generate_next_value_(name, start, count, last_values):
        return str.upper(name)

UpperStrEnum = AutoNameUpper

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

class AutoNameSnake2Camel(AutoName):
    """
    CamelStrEnum subclasses that create variants using `auto()` will have values equal to their camelCase names
    """
    def _generate_next_value_(name, start, count, last_values):
        return snake2camel(name, start_lower=True)



def transform(_class: Type[AutoName]=None, *, function: Callable[[str], str]=None):
    if function is None:
        raise ValueError(f"transform require `transform` function, pass it as a keyword argument.")

    def autoname_customized(class_: Type[AutoName]):
        function # this line makes the variable available at locals()
        class_name = class_.__name__
        unique_suffix = uuid.uuid4().hex
        root_class = f"AutoName_Customized_{unique_suffix}"
        transform_function_variableName = f"transform_{unique_suffix}"

        part1 = f"""global {class_name}, {root_class}, {transform_function_variableName}
                    {transform_function_variableName} = function

                    class {root_class}(AutoName):
                        def _generate_next_value_(name, start, count, last_values):
                            return {transform_function_variableName}(name)

                    class {class_name}({root_class}):

                    """
        part1 = inspect.cleandoc(part1)
        part2_classMembers = "".join([f"\t{v} = auto()\n" for v, obj in class_._member_map_.items()])
        exec(
            part1 + '\n' + part2_classMembers
        )
        return eval(class_name)

    if _class is None:
        return autoname_customized
    else:
        raise NotImplementedError("`_class` arg should not be specified.")
