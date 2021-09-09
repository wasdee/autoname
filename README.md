# autoname

<div align="center">

[![Build status](https://github.com/circleoncircles/autoname/workflows/build/badge.svg?branch=master&event=push)](https://github.com/circleoncircles/autoname/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/autoname.svg)](https://pypi.org/project/autoname/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/circleoncircles/autoname/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/circleoncircles/autoname/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/circleoncircles/autoname/releases)
[![License](https://img.shields.io/github/license/circleoncircles/autoname)](https://github.com/circleoncircles/autoname/blob/master/LICENSE)

a string enum `AutoName` from python docs with multiple stringcase options

</div>

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


print(GameType.INDIE.value)  # "INDIE"
```

## Alternative 
- `StrEnum` from [`fastapi-utils`](https://github.com/dmontagu/fastapi-utils)
## 🛡 License

[![License](https://img.shields.io/github/license/circleoncircles/autoname)](https://github.com/circleoncircles/autoname/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/circleoncircles/autoname/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{autoname,
  author = {circleoncircles},
  title = {a string enum `AutoName` from python docs with multiple stringcase options},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/circleoncircles/autoname}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)