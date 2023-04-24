# webscraping using selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# options allows you to set Chrome browser options
options = Options()

# detach means it allows chrome to run in a seperate window (set to true)
options.add_experimental_option('detach', True)

# driver uses google chrome as the web browser
driver = webdriver.Chrome(options=options)

# directing the driver to the desired url
driver.get('https://www.tiktok.com')


time.sleep(5)

login_string = """
    
"""

search_string = """
    //input[@placeholder='Search']
"""

# obtaining html using string specified above
dvr = driver.find_elements('xpath', search_string)

# # obtains the last pagination number to know how many pages to iterate through
for d in dvr:
    d.send_keys("#hello")
    d.send_keys(Keys.ENTER)

# driver.close()
