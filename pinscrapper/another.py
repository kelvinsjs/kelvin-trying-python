from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

var = "analytics"
url = "https://in.pinterest.com/search/pins/?q=" + var
ScrollNumber = 4  # The depth we wish to load
sleepTimer = 1    # Waiting 1 second for page to load

#  Bluetooth bug circumnavigate
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path='geckodriver.exe')
driver.get(url)

for _ in range(1, ScrollNumber):
    driver.execute_script("window.scrollTo(1,100000)")
    print("scrolling")
    time.sleep(sleepTimer)

soup = BeautifulSoup(driver.page_source, 'html.parser')

for link in soup.find_all('img'):
    print(link.get('src'))