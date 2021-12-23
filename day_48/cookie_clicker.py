from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1280, 720)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def click_on(c, number_of_clicks=100):
    n = number_of_clicks
    while n >= 0:
        c.click()
        n -= 1
    return True


cookie = driver.find_element(By.ID, value="cookie")

click_on(cookie, 20)
product0 = driver.find_element(By.ID, value="buyCursor")
product0.click()

# products = driver.find_elements(By.CLASS_NAME, value="product")
# for product in products:
#     if product.text == "Grandma\n100":
#         product.click()
#         print("Give me my Grandma")
#     print(product.text)

