#Identify actions : Control+A, Cpntrol+C, Tab,Control+V

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://text-compare.com/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()


Text_1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
Text_2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

Text_1.send_keys("Shweta's First Test Case")
act=ActionChains(driver)

#Control A action
act.key_down(Keys.CONTROL).send_keys("a").key_down(Keys.CONTROL).perform()

#Contol C action :-
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Tab key
act.key_down(Keys.TAB).perform()


#Control V action
act.key_down(Keys.CONTROL).send_keys("v").key_down(Keys.CONTROL).perform()

time.sleep(3)


