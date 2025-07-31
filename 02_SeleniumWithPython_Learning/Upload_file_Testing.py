import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def upload_file():
    from selenium.webdriver.chrome.service import Service
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

driver =upload_file()
driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys('C:/Test_files/Test.txt')
time.sleep(5)


