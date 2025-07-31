from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("http://www.deadlinkcity.com/")
driver.implicitly_wait(10)
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,'a')
count=0
for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print("This is broken URL -",url)
        count+=1
    else:
        print("This is not a broken URL -",url)
print("Broken link Count is - ",count)
driver.quit()
