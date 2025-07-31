import pytest
@pytest.fixture()
def chrome_setup():
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service
    # service = Service()
    # driver=webdriver.Chrome(service=service)
    # return driver
    print("Once before every method")
def test_launch_app(chrome_setup):
    print("launch_app Method-1")
    # driver = chrome_setup()
    # driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    # driver.maximize_window()
    # driver.implicitly_wait(5)
def test_close_app():
    #driver = chrome_setup()
    print("Close_app Method-2")
    #driver.quit()


# @pytest.fixture()
# def setup_module():
#     service=Service()
#     driver= webdriver.Chrome(service=service)
#     driver.get("https://www.google.com/")
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

def test_TestCase1_check_title(setup_module):
    driver=setup_module
    assert driver.title == 'Google'

def test_check_url(setup_module):
    driver = setup_module
    assert driver.current_url == "https://www.google.com/"
