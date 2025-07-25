import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://techbeamers.com/selenium-practice-test-page/")
driver.maximize_window()
time.sleep(3)

#is_displayed()
username_field=driver.find_element(By.XPATH, "//input[@id='username']")
print(username_field.is_displayed())

#is_enabled
print(username_field.is_enabled())

#driver.switch_to.frame("practiceForm")

radio_button=driver.find_element(By.XPATH,"//input[@id='male']").text
print("Name:",radio_button)
#radio_button.click()
#print(radio_button.is_selected())

