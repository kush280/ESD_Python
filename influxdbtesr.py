import os
from selenium import webdriver
import time
os.environ['webdriver.chrome.driver'] = '/path/to/chromedriver'
browser = webdriver.Chrome()
browser.get('localhost:8086')
time.sleep(5)
browser.quit()
