from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

#**************** IMPLICIT WAIT ********************#
driver.implicitly_wait(10)
#**************** IMPLICIT WAIT ********************#


driver.get("https://www.google.com/")
driver.maximize_window()


#**************** PYTHON DEFIND ********************#
#time.sleep(5)
#**************** PYTHON DEFIND ********************#

search_box=driver.find_element(By.ID,"APjFqb")
search_box.send_keys("Selenium")
search_box.submit()

link_sel=driver.find_element(By.XPATH,'//h3[text()="Selenium"]')
link_sel.click()


driver.quit()
