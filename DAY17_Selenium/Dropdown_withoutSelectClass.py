import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.implicitly_wait(5)
driver.maximize_window()

country_dropdown=driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")
country_dropdown.click()

country_dropdown_values=driver.find_elements(By.TAG_NAME,'option')


for country_dropdown_value in country_dropdown_values:
    if country_dropdown_value.get_attribute("value") == 'AGO':
        country_dropdown_value.click()
        break

time.sleep(5)

