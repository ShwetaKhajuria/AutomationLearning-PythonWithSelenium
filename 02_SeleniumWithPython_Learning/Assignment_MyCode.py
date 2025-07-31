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


from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


try:
    driver = uc.Chrome()
    driver.maximize_window()

    #Open website
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()

    #Email field
    Email_field= driver.find_element(by=By.ID,value="Email")
    Email_field.clear()
    Email_field.send_keys("admin@yourstore.com")

    #Password field
    Password_field=driver.find_element(by=By.ID,value="Password")
    Password_field.clear()
    Password_field.send_keys("admin")

    #Login button
    driver.find_element(by=By.XPATH,value='//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
    time.sleep(5)

    #Handling the "Are you human?" window
    for attempt in range(3):
        try:
            captcha_field=driver.find_element(by=By.XPATH,value='//input[@type="checkbox"]')
            captcha_field.click()
        except:
            print("There was no Captcha window appeared")

    #Capturing and comparing the window title with expected title
    Actual_WindowTitle=driver.title
    Expected_WindowTitle="Dashboard / nopCommerce administration"

    if Actual_WindowTitle==Expected_WindowTitle:
        print(f"Test case pass. The actual window title is: {Actual_WindowTitle}")
    else:
        print(f"The Test case Failed. The Actual window title was : {Actual_WindowTitle}")


finally:
   #driver.close() --- This was causing an issue handle is invalid so changed the below code
    try:
        driver.close()
    except Exception as e:
        print(f"Error closing driver: {e}")


