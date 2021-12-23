from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1280, 720)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Karamba")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Karambow")

email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("fake@email.it")

sign_up = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
sign_up.click()

# driver.quit()
