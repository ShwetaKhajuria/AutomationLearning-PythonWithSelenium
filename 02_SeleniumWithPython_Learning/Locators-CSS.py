import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service) # This wil Launch browser

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

# Tag and ID. [format: tag_name#ValueofID Ex-input#email]. Tag name is optional you can also specify [#email]
driver.find_element(by=By.CSS_SELECTOR,value='input#email').send_keys("shwetaknaik")
time.sleep(2)

# Tag and Class
driver.find_element(by=By.CSS_SELECTOR,value='input.inputtext').send_keys("@g")

# Tag and Attribute
driver.find_element(by=By.CSS_SELECTOR,value='input[data-testid=royal-email]').send_keys("mail.com")

# Tag, class , and Attribute
driver.find_element(by=By.CSS_SELECTOR,value= 'input.inputtext[data-testid=royal-pass]').send_keys("test")
time.sleep(5)



