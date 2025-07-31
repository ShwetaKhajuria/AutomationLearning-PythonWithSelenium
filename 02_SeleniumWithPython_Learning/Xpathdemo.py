import time
from pywinauto.keyboard import send_keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service= Service()
driver = webdriver.Chrome(service=service)

try:
    # driver.get("https://opensource-demo.orangehrmlive.com/")
    # driver.maximize_window()
    # time.sleep(2)
    # driver.find_element(by=By.NAME,value="username").send_keys("Admin")
    # driver.find_element(by=By.NAME,value="password").send_keys("admin123")
    # # Relative Xpath
    # driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()
    # time.sleep(2)
    # #Absolute XPath
    # driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/div[1]/div[1]/input[1]").send_keys("employee")
    driver.get("https://techbeamers.com/selenium-practice-test-page/")
    driver.maximize_window()
    time.sleep(2)
    # or operator
    driver.find_element(by=By.XPATH,value="//input[@id ='username' or @name='username'] ").send_keys("Admin")
    # and Operator
    driver.find_element(by=By.XPATH,value="//input[@id='email' and @name='email']").send_keys("shweta.khajuria@homehardware.ca")
    #or Operator
    driver.find_element(by=By.XPATH,value="//input[@id='password' or @name='password']").send_keys("admin")
    time.sleep(5)
    #Contains()
    driver.find_element(by=By.XPATH,value="//input[contains(@id,'password')]").clear()
    #Starts-with()
    driver.find_element(by=By.XPATH, value="//input[starts-with(@id,'pass')]").clear()
    #textmethod
    time.sleep(2)
   # driver.find_element(by=By.XPATH,value="//a[text()='password']").send_keys("abc")
finally:
    driver.close()
