import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

#driver.switch_to.frame("singleframe")
nested_frame=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(nested_frame)
Iframe_demo=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(Iframe_demo)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("New test")
time.sleep(1)

driver.switch_to.default_content()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[1]/a").click()
time.sleep(3)