import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#************* Creates a driver *************#
service=Service()
driver=webdriver.Chrome(service=service)


driver.get("https://practicesoftwaretesting.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#***************** select one checkbox ********************#
driver.find_element(By.XPATH,"//label[normalize-space()='Hand Tools']").click()
#***************** select one checkbox ********************#

driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()


#**************** Select Multiple Checkboxes ***********#
checkboxes=driver.find_elements(By.XPATH,"//form[@id='checkboxes']//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()

#**************** Select Multiple Checkboxes by Choice {THIS IS THE LOGIC ONLY WONT WORK ON THE TEST WEBSITE}***********#
for checkbox in checkboxes:
    check=checkbox.get_attribute('type')
    if check=='checkbox 1':
        checkbox.click()
time.sleep(5)


#**************** clearing all the checkboxes ***********#

driver.quit()
