import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Create driver obj
service=Service()
driver=webdriver.Chrome(service=service)


#Launch Website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

#Login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Open Dynamic table
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
time.sleep(5)


rows=driver.find_elements(By.XPATH,"//div[@role='row']")
print("Total number of rows",len(rows))
dis=0
enb=0

for r in range(1,len(rows)+1):
    column=driver.find_element(By.XPATH,"//div[@role='rowgroup']//div[1]//div[1]//div["+str(r)+"]")
    if column.text== "Disabled":
        dis+=1
    else:
        enb+=1
print("Disabled: ",dis)
print("Enabled: ",enb)
