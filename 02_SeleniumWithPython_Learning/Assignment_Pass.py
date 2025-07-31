# # Test case 2:-
# 1) Open web Browser
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3) Provide Email : admin@yourstore.com
# 4) Provide Password : admin
# 5) Click on Login
# 6) It will ask you to check a checkbox to verify if you are a human for 3 times. Check the checkbox everytime
# 6) Capture title of the dashboard page (Actual title)
# 7) Verify title of the page :"Dashboard /nonCommerce administration" (Expected)
# 8) Close browser
#

import time
import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context



try:
    # Step 1: Open Chrome browser (undetected)
    driver = uc.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://admin-demo.nopcommerce.com/login")

    # Step 3: Provide Email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Email"))
    )
    email_field.clear()
    email_field.send_keys("admin@yourstore.com")

    # Step 4: Provide Password
    password_field = driver.find_element(By.ID, "Password")
    password_field.clear()
    password_field.send_keys("admin")

    # Step 5: Click on Login
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    #Step 6: Handle "I'm not a robot" checkboxes 3 times (simulated retry)
    for attempt in range(3):
        try:
            # Try to find and click the checkbox (assuming a known XPath)
            checkbox = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="checkbox"]'))
            )
            checkbox.click()
            print(f"Checkbox clicked: Attempt {attempt + 1}")
            time.sleep(2)
        except:
            print(f"No checkbox found on attempt {attempt + 1}, possibly already passed.")
            break

    # Step 7: Capture and verify title
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
    actual_title = driver.title
    expected_title = "Dashboard / nopCommerce administration"

    if actual_title == expected_title:
        print("✅ Test Case Passed")
    else:
        print(f"❌ Test Case Failed. Actual title is: '{actual_title}'")

finally:
    driver.close()
