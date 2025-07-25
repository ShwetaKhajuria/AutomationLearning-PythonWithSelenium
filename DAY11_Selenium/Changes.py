# Test case 2:-
# 1) Open web Browser
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3) Provide Email : admin@yourstore.com
# 4) Provide Password : admin
# 5) Click on Login
# 6) It will ask you to check a checkbox to verify if you are a human for 3 times. Check the checkbox everytime
# 6) Capture title of the dashboard page (Actual title)
# 7) Verify title of the page :"Dashboard /nonCommerce administration" (Expected)
# 8) Close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #1
from selenium.webdriver.support import expected_conditions as EC #2
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException #3
import time
import undetected_chromedriver as uc
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


try:
    driver = uc.Chrome()
    driver.maximize_window()

    #Open website
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()

    #Email field operation #4
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Email")))
    email_field.clear()
    email_field.send_keys("admin@yourstore.com")

    #Password field operation
    Password_field=driver.find_element(by=By.ID,value="Password")
    Password_field.clear()
    Password_field.send_keys("admin")

    #Login button
    driver.find_element(by=By.XPATH,value='//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()


    #Handling the "Are you human?" window
    for attempt in range(3):
        try:
            checkbox = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="checkbox"]'))
            )
            checkbox.click()
            print(f"CAPTCHA checkbox clicked at attempt {attempt + 1}")
            break
        except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
            print(f"No CAPTCHA checkbox found or clickable on attempt {attempt + 1}")
            time.sleep(2)

    #Capturing and comparing the window title with expected title
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
    actual_title = driver.title
    expected_title = "Dashboard / nopCommerce administration"  # FIXED TYPO

    if actual_title == expected_title:
        print(f"✅ Test case passed. The actual window title is: {actual_title}")
    else:
        print(f"❌ Test case failed. The actual window title is: {actual_title}")


finally:
    driver.close()




