import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from price import *

STORE = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine", "buyElder Pledge"]
timeout = 300   # [seconds]
timeout_store = 3   # [seconds]
timeout_start = time.time()
timeout_start_store = time.time()

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1280, 720)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def buy(what):
    print(what)
    grandma = driver.find_element(By.ID, value=what)
    grandma.click()


def click_on(c):
    global timeout_start_store
    global timeout_store
    while time.time() < timeout_start + timeout:
        c.click()
        if time.time() > timeout_start_store + timeout_store:
            store = driver.find_element(By.CLASS_NAME, value="grayed")
            first_grayed = store.get_attribute('id')
            index_grayed = STORE.index(first_grayed)
            if 0 < index_grayed < len(STORE):
                timeout_start_store = time.time()
                timeout_store = int(math.ceil(timeout_store * 1.1))
                buy(STORE[index_grayed-1])
            elif index_grayed == 0:
                timeout_start_store = time.time()
                timeout_store = int(math.ceil(timeout_store * 1.5))
                buy(STORE[index_grayed])


cookie = driver.find_element(By.ID, value="cookie")

click_on(cookie)

driver.quit()
