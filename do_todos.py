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


driver.get(URL)

input_field = driver.find_element(*input_field_selector)
input_field.send_keys("Todo")

add_todo_button = driver.find_element(*add_todo_button_selector)
add_todo_button.click()

todo_field = driver.find_element(*todo_field_selector)
check_todo_button = driver.find_element(*check_todo_button_selector)
check_todo_button.click()

todo_field_description = driver.find_element(*todo_field_description_selector)
todo_field_description_style = todo_field_description.get_attribute("style")

if todo_field_description_style == "text-decoration: line-through;":
    print("Ok")
else:
    print("Error")


driver.get(URL)

input_field = driver.find_element(*input_field_selector)
add_todo_button = driver.find_element(*add_todo_button_selector)

for i in range(3, 0, -1):
    input_field.send_keys(f"Todo{i}")
    add_todo_button.click()

sort_button = driver.find_element(*sort_button_selector)
sort_button.click()

todo_first_field = driver.find_element(By.CSS_SELECTOR, '.todo-item:nth-child(2)')
todo_first_field_text = todo_first_field.text

if todo_first_field_text == "Todo1":
    print("Ok")
else:
    print("Error")


driver.get(URL)

todos_list = driver.find_element(*todos_list_selector)
input_field = driver.find_element(*input_field_selector)
input_field.send_keys("Todo")

add_todo_button = driver.find_element(*add_todo_button_selector)
add_todo_button.click()

todo_fields = todos_list.find_elements(*todo_field_selector)
todos_list_length_before = len(todo_fields)

todo_field = driver.find_element(*todo_field_selector)
check_todo_button = driver.find_element(*check_todo_button_selector)
check_todo_button.click()

delete_todo_button = driver.find_element(*delete_todo_button_selector)
delete_todo_button.click()

todo_fields = todos_list.find_elements(*todo_field_selector)
todos_list_length_after = len(todo_fields)

if todos_list_length_before - todos_list_length_after == 1:
    print("Ok")
else:
    print("Error")


driver.quit()


# add_todo
# check_todo
# sort todos
# delete_todo

# delete all todos -> add clear_button
