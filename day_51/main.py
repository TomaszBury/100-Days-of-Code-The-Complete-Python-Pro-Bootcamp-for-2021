from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1920, 1200)
# print(driver.get_window_size())

driver.get("https://www.python.org")
events_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

# for time in events_times:
#     print(time.text)

events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for name in events_name:
#     print(name.text)

events = {}

for n in range(0, len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_name[n].text
    }

print(events)

driver.quit()

