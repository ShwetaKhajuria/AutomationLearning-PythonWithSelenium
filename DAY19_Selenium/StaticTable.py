# 1) Count number of rows and Column
# 2) Read specific row and column data
# 3) Read all the rows and column data
# 4) Read data based on condition (list book name whose author is Mukesh)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service()
driver=webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# 1) Count number of rows and Column
rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody/tr")
print("No of rows : ",len(rows)-1)

columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
print("No of Columns :",len(columns))

# 2) Read specific row and column data
cell_value=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr[5]/td[1]")
print("Specific row and column data: ",cell_value.text)


# 3) Read all the rows and column data
print("Content in table :- ")
for r in range(2,len(rows)):
    for c in range(1,len(columns)):
        data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text)
    print()


# 4) Read data based on condition (list book name whose author is Mukesh)
print("Books from Mukesh are:")
for r in range(2,len(rows)+1):
    data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]")
    if data.text=="Mukesh":
        Bookname=(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]"))
        price=(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]"))
        print(Bookname.text,"    ", price.text)


