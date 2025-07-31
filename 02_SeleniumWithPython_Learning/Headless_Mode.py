
from selenium import webdriver


def Headless_Mode():
    from selenium.webdriver.chrome.service import Service
    service=Service()
    ops=webdriver.ChromeOptions()
    ops.add_argument("--headless")  # ✅ modern way (instead of deprecated .headless=True)
    # ops.add_argument("--disable-gpu")
    # ops.add_argument("--window-size=1920,1080")
    # ops.add_argument("--no-sandbox")
    # ops.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service,options=ops)
    return driver

driver =Headless_Mode()
driver.implicitly_wait(5)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
print(driver.title)
print(driver.current_url)
