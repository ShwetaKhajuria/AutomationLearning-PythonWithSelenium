import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service = Service()

    preference ={"download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preference)

    driver=webdriver.Chrome(service=service,options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    service = Service()

    preference ={"download.default_directory":location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preference)

    driver=webdriver.Edge(service=service,options=ops)
    return driver

driver=chrome_setup()
driver.get("https://www.sample-videos.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[4]/a[1]").click()
time.sleep(5)