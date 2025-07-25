from selenium import webdriver
import time
from selenium.webdriver.chrome.service import service, Service

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://www.google.com/maps")
driver.maximize_window()
time.sleep(2)
driver.get("https://www.amazon.com")

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.quit()