import pytest
from calculator import Calculator


@pytest.mark.parametrize("a,b,expected",
                         [
         pytest.param(2, 3, 5, id="two-positives"),
         pytest.param(0, 0, 0, id="all-zero"),
         pytest.param(-1, 1, 0, id="mixed-sign-cancel"),
         pytest.param(-2, -3, -5, id="two-negatives"),
         ],
         )
def test_add_with_ids(a, b, expected):
    assert Calculator().add(a, b) == expected


def test_div_by_zero_raises():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(10, 0)

@pytest.mark.parametrize("a,b,expected",
                         [
         pytest.param(5, 3, 2, id="two-positives"),
         pytest.param(0, 0, 0, id="all-zero"),
         pytest.param(-1, 1, -2, id="mixed-sign-cancel"),
         pytest.param(-2, -3, 1, id="two-negatives"),
         ],
         )
def test_sub_with_ids(a, b, expected):
    assert Calculator().sub(a, b) == expected
