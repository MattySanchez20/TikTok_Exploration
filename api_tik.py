from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/foryou")

print(driver.title)

driver.quit()

# testing to see changes