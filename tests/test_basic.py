import pytest
from calculator import Calculator

def test_add_0_0() -> None:
    c = Calculator()
    assert c.add(0, 0) == 0

def test_div_basic():
    calc = Calculator()
    assert calc.div(10, 2) == 5.0