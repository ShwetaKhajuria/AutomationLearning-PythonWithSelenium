import pytest

@pytest.fixture()
def setup():
    print("Once before Every Method")
    yield
    print("Once after every Method")

def test_method1(setup):
    print("This is Test method 1")

def test_method2(setup):
    print("This is Test method 2")