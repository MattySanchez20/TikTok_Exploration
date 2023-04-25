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

# detach means it allows chrome to run in a separate window (set to true)
options.add_experimental_option('detach', True)

# driver uses google chrome as the web browser
driver = webdriver.Chrome(options=options)

# directing the driver to the desired url
driver.get('https://www.tiktok.com')

# maximizes window
driver.maximize_window()

# makes the driver wait 10 seconds to allow popup to come up
wait = WebDriverWait(driver, 10)

# xpath to window close
window_close = "//div[@data-e2e='modal-close-inner-button']"

# once it has waited, it will click the close button (found by xpath)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, window_close)))

# clicks the close button
close_button.click()

# wait for search box to become visible
search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-e2e='search-user-input']")))

# scroll the search box into view
driver.execute_script("arguments[0].scrollIntoView();", search_box)

# send keys to search box
search_box.send_keys("#hello")

# submit the search query by pressing enter
search_box.send_keys(Keys.ENTER)