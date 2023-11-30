import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# For Chromium
from webdriver_manager.core.os_manager import ChromeType


from locators import *


URL = "https://aprotonics.github.io/To-do-list/"


driver = None
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--start-in-incognito")

# For Chrome
# service=Service(ChromeDriverManager().install())

# For Chromium
service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

driver.get(URL)


todo_description = "Todo"
input_field = driver.find_element(*input_field_selector)
input_field.send_keys(todo_description)

add_todo_button = driver.find_element(*add_todo_button_selector)
add_todo_button.click()

todo_field = driver.find_element(*todo_field_selector)
todo_field_description = driver.find_element(*todo_field_description_selector)
todo_field_description_text = todo_field_description.text

if todo_description == todo_field_description_text:
    print("Ok")
else:
    print("Error")

driver.quit()
