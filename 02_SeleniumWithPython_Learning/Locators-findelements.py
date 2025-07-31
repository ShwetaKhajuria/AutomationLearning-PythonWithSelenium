import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://jqueryui.com/selectable/")
driver.maximize_window()
time.sleep(5)

#Find Elements-Tag name
tags=driver.find_elements(by=By.TAG_NAME,value='a')
print(len(tags))

# switch to iframe
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)

#Find elements-Class name
sliders=driver.find_elements(by=By.CLASS_NAME,value='ui-selectee')
print(len(sliders))



