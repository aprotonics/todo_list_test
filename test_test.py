import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# For Chromium
from webdriver_manager.core.os_manager import ChromeType


from locators import *


URLs = ["https://bank1.com/", 
        "https://bank2.com/",
        "https://bank3.com/",
        "https://bank4.com/",
        "https://bank5.com/",
        "https://bank6.com/",
        "https://bank7.com/",
        "https://bank8.com/",
        "https://bank9.com/"
        ]


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


for i in range(len(URLs)):
    driver.get(URLs[i])

    order_button = driver.find_element()
    order_button.click()





driver.quit()
