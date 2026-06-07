import pytest
from single_app import classify_number

@pytest.mark.parametrize(
    "input_val, expected",
    [
        (1, "1"),
        (3, "fizz"),
        (5, "buzz"),
        (15, "fizzbuzz"),
        (0, "fizzbuzz"),
        (-3, "fizz"),
        (-5, "buzz"),
    ]
)
def test_classify_number(input_val, expected):
    assert classify_number(input_val) == expected