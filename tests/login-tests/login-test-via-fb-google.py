from ast import Assert
from re import T
from webbrowser import Chrome
from xml.dom.minidom import Element
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://kumparan.com/')
    time.sleep(3)
    yield driver
    # driver.quit()

def test_fb(driver):
    # Login
    print("Scenario: User login with facebook")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-login-fb"]').click()
    time.sleep(5)
    #Success open dialog login with faceboock
    assert "kumparan.com - Platform Media" in driver.title

def test_google(driver):
    # Login
    print("Scenario: User login with Google")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-login-google"]').click()
    time.sleep(10)
    #Success open dialog login with faceboock
    assert "kumparan.com - Platform Media" in driver.title
    