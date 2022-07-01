from ast import Assert
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

def test_case(driver):
    # Login
    print("Scenario: User success register")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@data-qa-id="btn-register"]').click()
    time.sleep(2)
    email = driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]')
    email.send_keys("uyaylluyhafila@gmail.com")
    email.send_keys(Keys.ENTER);
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()

def test_case2(driver):
    # Login
    print("Scenario: User failed to register when email was already registered")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@data-qa-id="btn-register"]').click()
    time.sleep(2)
    email = driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]')
    email.send_keys("yullyayu08@gmail.com")
    email.send_keys(Keys.ENTER);
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 dmeJVj"]//*[contains(text(),"Email sudah terdaftar")]')
    test.click()
    t = test.text
    assert "Email sudah terdaftar" in t

    