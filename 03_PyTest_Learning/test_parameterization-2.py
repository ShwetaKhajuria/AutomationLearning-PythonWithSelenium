import pytest
@pytest.mark.usefixtures(setup_module)

@pytest.mark.parametrize('url,title',
                         [('www.google.com','Google'),
                          ('www.facebook.com','Facebook'),
                          ('www.instagram.com','Instagram')])
def test_title(setup_module,url,title):
    """
    :param setup_module:
    :param url:
    :param title:
    :return:
    """
    driver=setup_module
    assert driver.title == title
