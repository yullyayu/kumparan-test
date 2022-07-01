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

def test_without_login(driver):
    time.sleep(3)
    print("Scenario: User can't add comment without login")
    assert "kumparan.com - Platform Media Berita Kolaboratif, Terkini Indonesia Hari Ini" in driver.title
    filename = time.strftime("%Y_%m_%d_%H%M%S")
    driver.save_screenshot("E:/Automation-test/website-test/Screenshots/Search Product/1."+filename+".png")
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@class, "LabelLinkweb__StyledLink-sc-fupmuj-0 btFwc sc-750vfa-1 dpxwI")]').click()
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[@data-qa-id="comment-button-wrapper"]//img[@class="Iconweb__StyledIcon-sc-zyhgsp-0 hqzPjB"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[contains(@class, "CommentEditorweb__EditorBorder-sc-1tnt9hh-0 dXNXZI")]//*[contains(@data-slate-node, "element")]').send_keys('Tes')

def test_add_comment(driver):
    print("Scenario: User can add comment")
    # Login
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@data-qa-id, "hd-login")]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-email"]').send_keys('yullyayu08@gmail.com')
    driver.find_element(By.XPATH, '//input[@data-qa-id="input-password"]').send_keys('08Juli98')
    driver.find_element(By.XPATH, '//button[@data-qa-id="btn-save"]').click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[@data-qa-id="comment-button-wrapper"]//img[@class="Iconweb__StyledIcon-sc-zyhgsp-0 hqzPjB"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@class, "CommentEditorweb__EditorBorder-sc-1tnt9hh-0 dXNXZI")]//*[contains(@data-slate-node, "element")]').send_keys('Tes')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@data-qa-id, "btn-send-comment")]')

    