from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service()
driver=webdriver.Chrome(service=service)

#**************** EXPLICIT WAIT - Declaration  ********************#
explicitewait=WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException])
#**************** EXPLICIT WAIT - Declaration  ********************#


driver.get("https://www.google.com/")
driver.maximize_window()
search_box=driver.find_element(By.ID,"APjFqb")
search_box.send_keys("Selenium")
search_box.submit()


#**************** EXPLICIT WAIT - Usage  ********************#
link_webelement=explicitewait.until(EC.presence_of_element_located((By.XPATH,'//h3[text()="Selenium"]')))
link_webelement.click()
#**************** EXPLICIT WAIT - Usage  ********************#

driver.quit()