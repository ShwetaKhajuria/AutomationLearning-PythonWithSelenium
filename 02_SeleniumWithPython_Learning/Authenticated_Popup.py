import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service=Service()
driver=webdriver.Chrome(service=service)

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.implicitly_wait(5)

time.sleep(4)