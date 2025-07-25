from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://techbeamers.com/selenium-practice-test-page/")
driver.maximize_window()

#Commands
print("Page title is-",driver.title)
print("Current URL is-",driver.current_url)
#print(driver.page_source)

