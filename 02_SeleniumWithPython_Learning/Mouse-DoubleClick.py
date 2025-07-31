import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()
driver.implicitly_wait(5)

Field1=driver.find_element(By.XPATH,"//input[@id='field1']")
Field1.clear()
Field1.send_keys("Shweta")

Copy_text_button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")


act=ActionChains(driver)
act.double_click(Copy_text_button).perform()
time.sleep(5)