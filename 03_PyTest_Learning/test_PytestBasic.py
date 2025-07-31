import pytest

@pytest.mark.smoke
def test_m1():
    a = 10
    b = 20
    assert a==b, "M1 Test case Failed"

def test_m2():
    assert True,"M2 Test case Passed "

@pytest.mark.smoke
def test_m3():
    assert "shweta" == "SHWETA"


def test_login_insta():
    assert True, "Insta login happend"
