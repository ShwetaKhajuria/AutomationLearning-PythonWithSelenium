import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://www.rediffmailpro.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//input[@value=' Login']").click()
alert_window1=driver.switch_to.alert
Actual_result=alert_window1.text
expected_result="Enter Credentials"

if Actual_result==expected_result:
    print("Your test case Passed!!!")
else:
    print("Your text case Failed!!!")
