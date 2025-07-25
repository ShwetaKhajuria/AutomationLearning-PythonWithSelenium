from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Bootstrap_dropdown():
    from selenium.webdriver.chrome.service import Service
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

driver =Bootstrap_dropdown()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
for country in countries:
    if country.text=="India":
        country.click()
        break
time.sleep(3)
