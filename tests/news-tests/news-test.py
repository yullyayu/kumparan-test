from webbrowser import Chrome
from selenium import webdriver
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
    driver.maximize_window()
    driver.get('http://kumparan.com/')
    time.sleep(3)
    yield driver
    driver.quit()

def test_case(driver):
    time.sleep(3)
    print("User can see news")
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@class, "LabelLinkweb__StyledLink-sc-fupmuj-0 btFwc sc-750vfa-1 dpxwI")]').click()
    time.sleep(5)
    
def test_news_trending_lainnya(driver):
    time.sleep(3)
    print("User can see other trending news")
    assert "kumparan.com - Platform Media Berita Kolaboratif, Terkini Indonesia Hari Ini" in driver.title
    driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-allow-button"]').click()
    driver.find_element(By.XPATH,'//*[contains(@class, "LabelLinkweb__StyledLink-sc-fupmuj-0 btFwc sc-750vfa-1 dpxwI")]').click()
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(3)
    driver.find_element(By.XPATH,'//a[@class="LabelLinkweb__StyledLink-sc-fupmuj-0 btFwc"]//button[@class="Buttonweb__StyledButton-sc-befmsf-0 bFvdOg"]').click()
    time.sleep(5)
    test = driver.find_element(By.XPATH,'//div[@class="Viewweb__StyledView-sc-1ajfkkc-0 cujJdZ"]//*[contains(text(),"Trending")]')
    test.click()
    t = test.text
    assert "Trending" in t