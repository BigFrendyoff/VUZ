from factorial import factorial, get_input
import pytest


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_get_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_input() == 5

    monkeypatch.setattr('builtins.input', lambda _: 'test')
    with pytest.raises(ValueError):
        get_input()

    monkeypatch.setattr('builtins.input', lambda _: '-1')
    with pytest.raises(ValueError):
        get_input()

pytest.main()