from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
time.sleep(2)

abc=driver.find_element(by=By.XPATH,value="//*/child::a").text
print(abc)
#driver.find_element(By.XPATH, "//div[@id='main']/child::p")

