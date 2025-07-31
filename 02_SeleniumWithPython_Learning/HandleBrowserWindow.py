import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

#*********************** Single window handle *******************************#
windowID=driver.current_window_handle
print("Current window ID :",windowID)
#*********************** Single window handle *******************************#

# Open a new tab by clicking
driver.find_element(By.XPATH,"//a[@href='https://www.facebook.com/OrangeHRM/']//*[name()='svg']").click()

#*********************** Multiple window handle *******************************#
windowIDs=driver.window_handles
#*********************** Multiple window handle *******************************#

#*********************** Operations on Mutiple window handles *****************
parentID=windowIDs[0]
print("Parent window ID :",parentID)
childID=windowIDs[1]
print("Child window ID :",childID)


driver.switch_to.window(parentID)
print("Parent Title :",driver.title)

time.sleep(5)
driver.switch_to.window(childID)
print("Child Title :",driver.title)

for windowID in windowIDs:
    driver.switch_to.window(windowID)
    time.sleep(2)
    print(driver.title)
    print(driver.current_url)
    if driver.title == "OrangeHRM":
        driver.close()





time.sleep(5)
driver.close()