from selenium.webdriver.common.by import By


input_field_selector = (By.CSS_SELECTOR, '.todo-new-item')
add_todo_button_selector = (By.CSS_SELECTOR, '.todo-add-button')
todos_list_selector = (By.CSS_SELECTOR, '.todo-list')
todo_field_selector = (By.CSS_SELECTOR, '.todo-item')
todo_field_description_selector = (By.CSS_SELECTOR, '.todo-item__text')
sort_button_selector = (By.CSS_SELECTOR, '.todo-headitem__text')
check_todo_button_selector = (By.CSS_SELECTOR, '.todo-item__box')
delete_todo_button_selector = (By.CSS_SELECTOR, '.todo-item__item-delete')
