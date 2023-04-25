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

# maximaises window
driver.maximize_window()

# makes the driver wait 10 seconds to allow popup to come up
wait = WebDriverWait(driver, 10)

# xpath to window close
window_close = """
    //div[@data-e2e='modal-close-inner-button']
"""

# once it has waited, it will click the close button (found by xpath)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, window_close)))

# clicks the close button
close_button.click()

# refresh
driver.refresh()

# xpath to input box
search_box = """
    //input[@name='q']
"""

# search = driver.find_element('xpath', search_box)

wait_for_search = WebDriverWait(driver, 10)


search = wait_for_search.until(
    EC.visibility_of_element_located(
        (
            By.XPATH, search_box
        )
    )
)

# search.send_keys('#hello')
# search.send_keys(Keys.ENTER)
