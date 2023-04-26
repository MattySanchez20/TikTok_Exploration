# webscraping using selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
close_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH, window_close
        )
    )
)

# clicks the close button
close_button.click()

# refreshes page because if it doesn't, it can't find the search box xpath
driver.refresh()

# xpath to input box
search_box = """
    //input[@name='q']
"""

# creating a webdriver wait class instance that waits for 10 seconds
wait_for_search = WebDriverWait(driver, 10)

# waits until selenium can find the search box xpath
search = wait_for_search.until(
    EC.visibility_of_element_located(
        (
            By.XPATH, search_box
        )
    )
)


# entering #hello into the search box
search.send_keys('#hello')

# hits enter in the search box to search for result
search.send_keys(Keys.ENTER)

# xpath to find the login via phone or email button
use_phone_xpath = """
    //a[@href='/login/phone-or-email']
"""

# while true, keep scrolling until the driver has found the use_phone_xpath
while True:
    try:
        popup_element = driver.find_element('xpath', use_phone_xpath)
        driver.execute_script("arguments[0].scrollIntoView();", popup_element)
        break
    except:
        ActionChains(driver).key_down(Keys.DOWN).perform()

# click on use phone number to log in button
popup_element.click()

# xpath to find phone number placeholder
enter_phone_xpath = """
    //input[@placeholder='Phone number']
"""

# find the phone number placeholder element
enter_phone_dvr = driver.find_element('xpath', enter_phone_xpath)

# enter phone number into phone number placeholder
enter_phone_dvr.send_keys('07447991035')

# xpath for aria expanded to find phone code extension (+44)
phone_extension_dropdown_xpath = """
    //div[@class='tiktok-1nc4fij-DivAreaSelectionContainer ewblsjs3']
"""

# find the dropdown menu via xpath
p_extension_dropdown_dvr = driver.find_element(
    'xpath',
    phone_extension_dropdown_xpath
)

# click the dropdown menu to show search box to type in country
p_extension_dropdown_dvr.click()

# xpath to find country code search box country
phone_extension_dropdown_input_xpath = """
    //input[@id='login-phone-search']
"""

# find country code search box element
phone_extension_dropdown_input_xpath_dvr = driver.find_element(
    'xpath',
    phone_extension_dropdown_input_xpath
)

# enters united kingdom in country code search box
phone_extension_dropdown_input_xpath_dvr.send_keys('united kingdom')

# sends enter key to country code search box
phone_extension_dropdown_input_xpath_dvr.send_keys(Keys.ENTER)

# finds send code button via xpath
send_code_xpath = """
    //button[@data-e2e='send-code-button']
"""

# finds the send code button element
send_code_dvr = driver.find_element('xpath', send_code_xpath)

# clicks send code button element
send_code_dvr.click()
