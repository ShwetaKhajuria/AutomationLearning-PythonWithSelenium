import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(5)
driver.maximize_window()

#Scroll down Pixel number
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Value", value)
time.sleep(5)

#Scroll down to the webelement
India=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",India)
value=driver.execute_script("return window.pageYOffset;")
print("Value", value)


#Scroll down to the End
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#Scroll up  to the start
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)