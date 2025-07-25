import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(0)

#simple way :-
driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("05/05/2026")

#By logic
year="2026"
Month="05"
Date= "05"

driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()

