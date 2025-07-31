# Test Case 1:-
# 1) Open a web Browser
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Provide Username: Admin
# 4) Provide Password: admin123
# 5) Click on Login
# 6) Capture the title of the home page (Actual title)
# 7) Verify the title of the page: OrangeHRM(expected)
# 8) Close the browser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Importing By class
import time

# Initialize the ChromeDriver service
#service = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
service = Service()
driver = webdriver.Chrome(service=service)

# Open the web page
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

password_field =driver.find_element(By.NAME,"password")
password_field.send_keys("admin123")

#driver.find_element(By.CLASS_NAME,".oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]")
login_button.click()

time.sleep(5)

actual_title=driver.title
expected_title="OrangeHRM"

if actual_title==expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()
