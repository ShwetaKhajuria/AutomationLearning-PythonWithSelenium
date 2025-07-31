import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min= driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max= driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')

print("Location before the moving")
print(min.location) #{'x': 59, 'y': 250}
print(max.location) #{'x': 767, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min,100,0).perform()
act.drag_and_drop_by_offset(max,-500,0).perform()

time.sleep(5)

print("Location after the moving")
print(min.location) #{'x': 158, 'y': 250}
print(max.location) #{'x': 265, 'y': 250}