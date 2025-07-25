
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(5)
# time.sleep(5)

driver.maximize_window()

link=driver.find_element(By.LINK_TEXT,"Digital downloads")

links=driver.find_elements(By.TAG_NAME,"a")
print("with tage name :",len(links))

links2=driver.find_elements(By.XPATH,"//a")
print("with tage name :",len(links2))

# Print all the links
for link3 in links2:
    print(link3.text)
