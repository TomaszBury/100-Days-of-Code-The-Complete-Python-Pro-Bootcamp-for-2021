import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from price import *

STORE = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine", "buyElder Pledge"]
timeout = 300   # [seconds]
timeout_store = 10   # [seconds]
timeout_start = time.time()
timeout_start_store = time.time()

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1280, 720)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def buy_factory():
    factory = driver.find_element(By.ID, value="buyFactory")
    factory.click()


def buy(what):
    print(what)
    grandma = driver.find_element(By.ID, value=what)
    grandma.click()


def click_on(c, m, number_of_clicks=1233):
    global timeout_start_store
    n = number_of_clicks
    while time.time() < timeout_start + timeout:
        c.click()
        n -= 1
        if time.time() > timeout_start_store + timeout_store:
            store = driver.find_element(By.CLASS_NAME, value="grayed")
            print(store.text)
            first_grayed = store.get_attribute('id')
            print(first_grayed)
            index_grayed = STORE.index(first_grayed)
            print(index_grayed)
            if index_grayed > 0:
                timeout_start_store = time.time()
                buy(STORE[index_grayed-1])


cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

click_on(cookie, money)
# grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
# print(grandma.get_attribute('id'))
# grandma_class = driver.find_element(By.ID, value="buyGrandma")
# print((grandma_class.get_attribute('class')))
# print(grandma.text.split(" ")[2])

# store = driver.find_element(By.CLASS_NAME, value="grayed")
# print(store)
# for item in store:
#     print(item.get_attribute('id'))

driver.quit()

# products = driver.find_elements(By.CLASS_NAME, value="product")
# for product in products:
#     if product.text == "Grandma\n100":
#         product.click()
#         print("Give me my Grandma")
#     print(product.text)

