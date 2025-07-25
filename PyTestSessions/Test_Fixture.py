import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import none_of


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

