from autoname import *

def test_normal_autoname():
    class Foo(AutoName):
        Final = auto()
        really = auto()
        KIDDING = auto()

    v1 = Foo.Final
    assert v1.value == 'Final'

    v2 = Foo.KIDDING 
    assert v2.value == 'KIDDING'