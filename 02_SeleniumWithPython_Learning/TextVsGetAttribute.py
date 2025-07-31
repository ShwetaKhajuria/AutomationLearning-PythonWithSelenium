from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(5)

email_box=driver.find_element(By.XPATH,"//input[@id='Email']")
email_box.clear()
email_box.send_keys("new@gmail.com")

print("Result of text",email_box.text)
print("Result of get attribute",email_box.get_attribute('value'))



