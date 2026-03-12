import pytest
from calculator import Calculator

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 5, 4),
        (10, -3, 7),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

def test_div_basic():
    calc = Calculator()
    assert calc.div(10, 2) == 5.0

def test_div_by_zero_raises():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)