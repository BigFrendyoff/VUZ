import hypothesis.strategies as st
from hypothesis import given


def distance(x1, y1, x2, y2):
    return ((x2 + x1) ** 2 - (y2 + y1) ** 2) ** 0.25


def correct_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1 / 2


@given(st.floats(), st.floats(), st.floats(), st.floats())
def test_distance(x1, y1, x2, y2):
    assert distance(x1, y1, x2, y2) >= 0


@given(st.floats(), st.floats(), st.floats(), st.floats())
def test_correct_distance(x1, y1, x2, y2):
    assert correct_distance(x1, y1, x2, y2) >= 0


# test_distance()
test_correct_distance()

# print(distance(0, 0, 0, 1))
