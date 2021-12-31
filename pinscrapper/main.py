from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import random
import requests

var = "analytics"
ScrollNumber = 2
sleepTimer = 1.5

# link['href']
with webdriver.Firefox() as driver:
    pinsArray = []
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.pinterest.com/grishakelvin/delete-me-from-this-planet/")
    for _ in range(1, ScrollNumber):
        driver.execute_script(f"window.scrollTo(0, 150000)")
        print("scrolling")
        time.sleep(sleepTimer)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for el in soup.findAll('img', attrs={'srcset': True}):
        print(el['srcset'])