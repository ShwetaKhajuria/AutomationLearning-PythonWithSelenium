from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.ie.service import Service


def get_Screenshot():
    from selenium.webdriver.chrome.service import Service
    service=Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.save_screenshot(os.getcwd()+"/screenshot.jpg")
    driver.get_screenshot_as_file(os.getcwd()+"/screenshot.jpg")
    return driver



driver = get_Screenshot()

