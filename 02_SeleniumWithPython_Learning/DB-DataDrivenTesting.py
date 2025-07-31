import time
import _mysql_connector
import _sqlite3
import mysql
from Utils_IMP import ExcelUtils
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Utils_IMP import ExcelUtils

service=Service()
driver=webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://www.geeksforgeeks.org/finance/fd-calculator/")
driver.maximize_window()

#con=mysql.co

rows = 0
for r in range(2,rows+1):
    Depo = ExcelUtils.readData(file,'Sheet1',r,1)
    Tenuer = ExcelUtils.readData(file,'Sheet1',r,2)
    Irate = ExcelUtils.readData(file,'Sheet1',r,3)
    Expected_Value = ExcelUtils.readData(file,'Sheet1',r,4)
    print(f"Row {r} -> Depo: {Depo}, Tenuer: {Tenuer}, Irate: {Irate}, Expected: {Expected_Value}")

    #To enter data and pressing Enter on the website.
    driver.find_element(By.XPATH,"//input[@id='deposit_amount']").send_keys(Depo)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(Tenuer)
    driver.find_element(By.XPATH, "//input[@id='interest_rate']").send_keys(Irate + Keys.TAB)
    act_value= driver.find_element(By.XPATH,"//span[@class='value principal_amount']").text

    #Validation
    if float(Expected_Value)==float(act_value):
        print("Test Passed")
    else:
        print("Test Failed")

    time.sleep(3)

driver.quit()



