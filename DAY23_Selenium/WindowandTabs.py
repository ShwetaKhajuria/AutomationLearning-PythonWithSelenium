import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def tab():
    from selenium.webdriver.chrome.service import Service
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    driver.switch_to.new_window('Tab')
    driver.get("https://testautomationpractice.blogspot.com/")
    return driver

def window():
    from selenium.webdriver.chrome.service import Service
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    driver.switch_to.new_window('window')
    driver.get("https://testautomationpractice.blogspot.com/")
    return driver


driver =tab()
driver =window()
time.sleep(5)