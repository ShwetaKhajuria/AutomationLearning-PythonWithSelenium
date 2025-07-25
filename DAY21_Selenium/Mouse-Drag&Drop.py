import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()

source_element=driver.find_element(By.ID,"draggable")
target_element=driver.find_element(By.ID,"droppable")

act=ActionChains(driver)
act.drag_and_drop(source_element,target_element).perform()

time.sleep(5)