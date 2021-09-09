from enum import auto

import pytest

from autoname import *


def test_normal_autoname():
    class Foo(AutoName):
        Final = auto()
        really = auto()
        KIDDING = auto()
        HolyCow = auto()
        whatTheMeow = auto()

    assert Foo.Final.value == "Final"
    assert Foo.really.value == "really"
    assert Foo.KIDDING.value == "KIDDING"
    assert Foo.HolyCow.value == "HolyCow"
    assert Foo.whatTheMeow.value == "whatTheMeow"


def test_lower_autoname():
    class Foo(AutoNameLower):
        Final = auto()
        really = auto()
        KIDDING = auto()
        HolyCow = auto()
        whatTheMeow = auto()

    assert Foo.Final.value == "final"
    assert Foo.really.value == "really"
    assert Foo.KIDDING.value == "kidding"
    assert Foo.HolyCow.value == "holycow"
    assert Foo.whatTheMeow.value == "whatthemeow"


def test_upper_autoname():
    class Foo(AutoNameUpper):
        Final = auto()
        really = auto()
        KIDDING = auto()
        HolyCow = auto()
        whatTheMeow = auto()

    assert Foo.Final.value == "FINAL"
    assert Foo.really.value == "REALLY"
    assert Foo.KIDDING.value == "KIDDING"
    assert Foo.HolyCow.value == "HOLYCOW"
    assert Foo.whatTheMeow.value == "WHATTHEMEOW"


def test_alias_StrEnum():
    class Foo(StrEnum):
        Final = auto()
        really = auto()
        KIDDING = auto()
        HolyCow = auto()
        whatTheMeow = auto()

    assert Foo.Final.value == "Final"
    assert Foo.really.value == "really"
    assert Foo.KIDDING.value == "KIDDING"
    assert Foo.HolyCow.value == "HolyCow"
    assert Foo.whatTheMeow.value == "whatTheMeow"


def test_autoname_decorator():
    @transform(function=str.lower)
    class Foo(StrEnum):
        Final = auto()
        really = auto()
        KIDDING = auto()
        HolyCow = auto()
        whatTheMeow = auto()

    assert Foo.Final.value == "final"
    assert Foo.really.value == "really"
    assert Foo.KIDDING.value == "kidding"
    assert Foo.HolyCow.value == "holycow"
    assert Foo.whatTheMeow.value == "whatthemeow"

    @transform(function=str.upper)
    class Foo(AutoName):
        Final = auto()
        really = auto()
        KIDDING = auto()
        HolyCow = auto()
        whatTheMeow = auto()

    assert Foo.Final.value == "FINAL"
    assert Foo.really.value == "REALLY"
    assert Foo.KIDDING.value == "KIDDING"
    assert Foo.HolyCow.value == "HOLYCOW"
    assert Foo.whatTheMeow.value == "WHATTHEMEOW"


def test_autoname_decorator_no_transform():
    with pytest.raises(ValueError) as excinfo:

        @transform
        class Foo(StrEnum):
            Final = auto()
            really = auto()
            KIDDING = auto()
            HolyCow = auto()
            whatTheMeow = auto()

        assert "" in str(excinfo.value)
