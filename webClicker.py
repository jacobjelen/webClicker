
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
browser.get('https://www.spareroom.com')
time.sleep(5)
browser.quit()