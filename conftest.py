import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup_module():
    service=Service()
    driver= webdriver.Chrome(service=service)
    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()