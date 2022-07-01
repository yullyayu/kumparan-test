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

def test_login(driver):
    # Login
    print("Scenario: User success Login")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('yullyayu08@gmail.com')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('08Juli98')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    time.sleep(3)

def test_without_register(driver):
    # Login
    print("Scenario: User can't login when user not yet registered")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('yullyayu07@gmail.com')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('lala8910')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    #validate error message
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 dmeJVj"]//*[contains(text(),"Email atau Password Salah")]')
    test.click()
    t = test.text
    assert "Email atau Password Salah" in t

def test_login_without_email(driver):
    # Login
    print("Scenario: User can't login without input email")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('08Juli98')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    #validate error message
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 dmeJVj"]//*[contains(text(),"Tidak boleh kosong")]')
    test.click()
    t = test.text
    assert "Tidak boleh kosong" in t

def test_login_without_password(driver):
    # Login
    print("Scenario: User can't login without input password")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('yullyayu08@gmail.com')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    #validate error message
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 dmeJVj"]//*[contains(text(),"Tidak boleh kosong")]')
    test.click()
    t = test.text
    assert "Tidak boleh kosong" in t

def test_login_format_notmatch(driver):
    # Login
    print("Scenario: User can't login when the email format not match")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('yullyayu08@.com')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('08Juli98')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    #validate error message
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 dmeJVj"]//*[contains(text(),"Harus diisi dengan format email")]')
    test.click()
    t = test.text
    assert "Harus diisi dengan format email" in t

def test_login_lessthan_character_password(driver):
    # Login
    time.sleep(5)
    print("Scenario: User can't login when the password lest than character")
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('yullyayu08@gmail.com')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('08Juli9')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    #validate error message
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 dmeJVj"]//*[contains(text(),"Minimal 8 karakter")]')
    test.click()
    t = test.text
    assert "Minimal 8 karakter" in t


    