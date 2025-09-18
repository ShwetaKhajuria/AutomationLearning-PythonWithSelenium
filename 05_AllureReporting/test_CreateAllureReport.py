import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@allure.severity(allure.severity_level.NORMAL)
def test_checklogo(): #Test case status-Pass
        service=Service()
        driver=webdriver.Chrome(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        driver.implicitly_wait(5)
        status=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img').is_displayed()
        if status == True:
            assert True
        else:
            allure.attach(driver.get_screenshot_as_file("Reports/Allure_Reports"),name="Homepage_checklogo",attachment_type=AttachmentType.PNG)
            driver.quit()
            assert False
@allure.severity(allure.severity_level.MINOR)
def test_UserName():
    pytest.skip("Part of next Sprint")

@allure.severity(allure.severity_level.CRITICAL)
def test_Login():
    service=Service()
    driver=webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    current_title=driver.title
    expected_title = "123" # OrangeHRM
    if current_title==expected_title:
        assert True
    else:
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="test_Login",
                        attachment_type=AttachmentType.PNG)
        assert False

