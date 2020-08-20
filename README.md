# autoname

an enum `AutoName` from [python docs](https://docs.python.org/3/library/enum.html#using-automatic-values) with multiple stringcase options.

## Get Started

```bash
$ pip install autoname
```

```python
from autoname import Autoname
from enum import auto

# an enum class
class GameType(AutoName):
    INDIE = auto()

print(GameType.INDIE.value) # "INDIE"

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
class GameType(AutoNameLower):
    INDIE = auto()

print(GameType.INDIE.value) # "indie"
```
