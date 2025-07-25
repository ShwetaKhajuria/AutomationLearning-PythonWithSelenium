import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(3)

alert_window=driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("This is test")
time.sleep(3)
# alert_window.accept()


alert_window.dismiss()
time.sleep(3)