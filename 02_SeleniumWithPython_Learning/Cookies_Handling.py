from tkinter.font import names

from selenium import webdriver
from selenium.webdriver.common.by import By


def cookie_handling():
    from selenium.webdriver.chrome.service import Service
    service=Service()
    driver=webdriver.Chrome(service=service)
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    cookies=driver.get_cookies()
    print(len(cookies))
    return driver

driver=cookie_handling()
cookies = driver.get_cookies()
# To get length
print(len(cookies))

#To Print cookies
# for cookie in cookies:
#     print(cookie)

#To add cookies
driver.add_cookie({'name': 'MY-COOKIES','value': '98989'})
cookies = driver.get_cookies()
print(len(cookies))
for cookie in cookies:
    print(cookie)

#To delete cookies
# driver.delete_cookie('MY-COOKIES')
# cookies = driver.get_cookies()
# print(len(cookies))
# for cookie in cookies:
#     print(cookie)