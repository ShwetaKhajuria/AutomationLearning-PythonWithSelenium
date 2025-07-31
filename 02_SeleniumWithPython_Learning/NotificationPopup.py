import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disabled-notification")

service=Service()
driver=webdriver.Chrome(service=service,options=ops)

driver.get("https://iplocation.io/my-location")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(5)

