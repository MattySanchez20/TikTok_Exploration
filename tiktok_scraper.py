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

# makes the driver wait 10 seconds to allow popup to come up
wait = WebDriverWait(driver, 10)

# once it has waited, it will click the close button (found by xpath)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-e2e='modal-close-inner-button']")))

# clicks the close button
close_button.click()
