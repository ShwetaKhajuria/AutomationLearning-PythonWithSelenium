import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.implicitly_wait(20)
driver.maximize_window()

country_dropdown=driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")

#**************    Using Select Class ********************* #
dropdown_options=Select(country_dropdown)

#Select options from the dropdown
dropdown_options.select_by_visible_text("India")
time.sleep(1)
dropdown_options.select_by_value("AGO")
time.sleep(1)
dropdown_options.select_by_index(10)

#Capture  all the options
no_of_options= dropdown_options.options
print(len(no_of_options))

#Display all the options
for no_of_option in no_of_options:
    print(no_of_option.text)
#**************    Using Select Class ********************* #

