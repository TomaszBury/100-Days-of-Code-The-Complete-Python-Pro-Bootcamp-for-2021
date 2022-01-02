# Form https://forms.gle/S8cozQ765rdUaUXx7
# Zillow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

google_form = "https://forms.gle/S8cozQ765rdUaUXx7"
otodom_lodz = "https://www.otodom.pl/pl/oferty/sprzedaz/dom/lodz?distanceRadius=15"

olx_lodz_dom = "https://www.olx.pl/nieruchomosci/domy/sprzedaz/lodz/?search%5Bdist%5D=15"

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.set_window_size(1280, 720)
driver.get(olx_lodz_dom)

titles = driver.find_elements(By.CSS_SELECTOR, value="h3 a strong")
prices = driver.find_elements(By.CSS_SELECTOR, value=".price strong")
locations = driver.find_elements(By.CSS_SELECTOR, value="p .breadcrumb span")
links = driver.find_elements(By.CSS_SELECTOR, value="td div h3 a")
data_to_save = []
house = {
        "title": 0,
        "price": 0,
        "location": 0,
        "link": ""
    }
index = 0
for title in titles:
    index = titles.index(title)
    # print(title.text)
    # print(prices[index].text)
    # print(locations[index * 2].text)
    # print(links[index].get_attribute("href"))

    house["title"] = title.text
    house["price"] = prices[index].text
    house["location"] = locations[index * 2].text
    house["link"] = links[index].get_attribute("href")
    # print(house)
    data_to_save.append(house.copy())

# print(data_to_save)
list_of_keys = ["title", "price", "location", "link"]
for d in data_to_save:
    driver.get(google_form)
    answers = driver.find_elements(By.CLASS_NAME, value="quantumWizTextinputPaperinputInput")
    time.sleep(2)
    for answer in answers:
        answer.click()
        answer.send_keys(d[list_of_keys[answers.index(answer)]])

    submit = driver.find_element(By.CLASS_NAME, value="appsMaterialWizButtonPaperbuttonLabel")
    submit.click()

driver.quit()
