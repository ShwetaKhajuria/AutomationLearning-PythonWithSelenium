import pytest

@pytest.mark.parametrize("a,b,expected",
                         [(1, 3, 4),
                          (8, 2, 5),
                          (4, 8, 9)])
def test_addition(a,b,expected):
    assert a + b == expected



