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


driver=chrome_setup()
driver.get("https://www.sample-videos.com/download-sample-pdf.php")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='download_pdf']").click()
time.sleep(5)