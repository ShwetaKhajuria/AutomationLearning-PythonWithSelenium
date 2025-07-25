from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest



def test_google():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == "Facebook - log in or sign up"
    driver.quit()

def test_gmail():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.gmail.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == "Gmail"
    driver.quit()

def test_redif():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.rediff.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Rediff Gurus"
    driver.quit()

