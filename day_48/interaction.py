from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1280, 720)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, value="All portals")
# all_portals.click()

search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

# driver.quit()
