#Locators
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)


#ID Locator
driver.find_element(by=By.ID,value='user-name').send_keys("standard_user")


#Name locator
driver.find_element(by=By.NAME,value='password').send_keys("secret_sauce")
driver.find_element(by=By.NAME,value='login-button').click()
time.sleep(5)


#ID Locator again
driver.find_element(by=By.ID,value='react-burger-menu-btn').click()
time.sleep(2)

# Partial Link text
# driver.find_element(by=By.PARTIAL_LINK_TEXT,value='Abou')
# time.sleep(10)

# Link text
driver.find_element(by=By.LINK_TEXT, value='About').click()

#Another website
driver.get("https://nopcommerce.com")
time.sleep(5)












