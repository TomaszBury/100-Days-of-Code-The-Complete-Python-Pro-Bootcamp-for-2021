from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1920, 1200)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.XPATH, value="/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

driver.quit()
