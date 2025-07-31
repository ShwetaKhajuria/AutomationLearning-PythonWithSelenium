import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Create driver obj
service=Service()
driver=webdriver.Chrome(service=service)


#Launch Website
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)


Point_me=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
mobile_option=driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")

#create an object of mouse action class
act=ActionChains(driver)
act.move_to_element(Point_me).move_to_element(mobile_option).click().perform()
time.sleep(5)


