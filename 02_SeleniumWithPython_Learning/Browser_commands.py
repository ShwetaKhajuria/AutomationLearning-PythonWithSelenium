import time

from pywinauto.findwindows import find_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service= Service()
driver=webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)

driver.close()


# Set up the Chrome driver
service = Service()
driver = webdriver.Chrome(service=service)

# Go to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)


# Click the 'OrangeHRM, Inc' link which opens in a new tab
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)

# Get the window handles (tabs)
tabs = driver.window_handles
print("Tabs:", tabs)

# Switch to the newly opened tab
driver.switch_to.window(tabs[1])
print("Switched to new tab:", driver.title)

# Perform actions in the new tab or just wait
time.sleep(3)

# Optional: Close the new tab
driver.close()

# Switch back to the original tab
driver.switch_to.window(tabs[0])
print("Back to original tab:", driver.title)

# Keep browser open (remove driver.quit() or driver.close())
input("Press Enter to close browser...")

# When ready, quit the browser completely
#driver.quit()