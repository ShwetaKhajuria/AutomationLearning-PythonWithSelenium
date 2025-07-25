from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)

#Scenario-1 - FindelemenT vs FindElemenTS- Locator matching with single element
element1=driver.find_element(by=By.XPATH,value="//input[@id='small-searchterms']")
element1.send_keys("test")
elements1=driver.find_elements(by=By.XPATH,value="//input[@id='small-searchterms']")
elements1[0].send_keys("testq")

# #Scenrio-2 - FindelemenT vs FindElemenTS- Locator matching with multiple webelements
element2=driver.find_element(by=By.XPATH,value='//div[@class="footer"]//a')
print(element2.text)
elements2=driver.find_elements(by=By.XPATH,value='//div[@class="footer"]//a')
for el in elements2:
    print(el.text)

#Scenario-3 - FindelemenT vs FindElemenTS- Element is not available - NoSuchElementException
element3=driver.find_element(by=By.XPATH,value="//input[@id='small-searchtermwws']")
elements3=driver.find_elements(by=By.XPATH,value="//input[@id='small-searchtermwws']")
print(len(elements3))

