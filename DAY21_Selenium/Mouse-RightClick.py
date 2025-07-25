import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Create driver obj
service=Service()
driver=webdriver.Chrome(service=service)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(5)

right_click_button =driver.find_element(By.XPATH,"//span[@Class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)
act.context_click(right_click_button).click().perform()
time.sleep(5)