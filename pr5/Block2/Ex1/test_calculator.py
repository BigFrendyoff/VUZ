import pytest
from calculator import add, subtract

@pytest.fixture
def numbers():
    return 3, 5

def test_add(numbers):
    assert add(*numbers) == 8

def test_subtract(numbers):
    assert subtract(*numbers) == -1

@pytest.mark.parametrize("operator, expected_result", [("add", 7), ("subtract", -2)])
def test_calculator(numbers, operator, expected_result):
    if operator == "add":
        assert add(*numbers) == expected_result
    elif operator == "subtract":
        assert subtract(*numbers) == expected_result


pytest.main()