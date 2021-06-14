
# autoname

an enum `AutoName` from [python docs](https://docs.python.org/3/library/enum.html#using-automatic-values) with multiple stringcase options.

## Get Started

```bash
$ pip install autoname
```

```python
from autoname import AutoName
from enum import auto


# an enum class
class GameType(AutoName):
    INDIE = auto()


print(GameType.INDIE.value)  # "INDIE"

# could be alternative in pydantic instead of literal
from pydantic import BaseModel


class Game(BaseModel):
    type: GameType
```

Also have others stringcases coverter
1. `AutoNameLower` - convert name value to lowercase
2. `AutoNameUpper` - convert name value to uppercase

e.g.
```python
from autoname import AutoNameLower
from enum import auto

class GameType(AutoNameLower):
    INDIE = auto()

print(GameType.INDIE.value) # "indie"
```

You could also bring your own case convertion algorithm.

```python
from autoname import AutoName, transform
from enum import auto


@transform(function=str.lower)
class GameType(AutoName):
    INDIE = auto()


print(GameType.INDIE.value)  # "indie"
```

If the `autoname` is not a sound variable name. there are alias too.
- `StrEnum` = `AutoName`
- `LowerStrEnum` = `AutoNameLower`
- `UpperStrEnum` = `AutoNameUpper`

e.g.
```python
from autoname import StrEnum, transform
from enum import auto


class GameType(StrEnum):
    INDIE = auto()


print(GameType.INDIE.value)  # "indie"
```

## Alternative 
- `StrEnum` from [`fastapi-utils`](https://github.com/dmontagu/fastapi-utils)
