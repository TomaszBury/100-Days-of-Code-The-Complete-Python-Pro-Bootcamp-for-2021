from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# driver.get("https://www.amazon.com/")
# driver.get("https://www.amazon.com/Instant-Pot-Air-Fryer-One-Touch/dp/B07VT23JDM/ref=sr_1_6?qid=1640157112")
# price = driver.find_element(value="price_inside_buybox")
# print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# # print(search_bar.tag_name)
# print((search_bar.get_attribute("placeholder")))

# logo = driver.find_element(By.CLASS_NAME, value="python-logo")
# print(logo.get_attribute("src"))
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# print(documentation_link.get_attribute("href"))

# submit_bug = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(submit_bug.text)
# print(submit_bug.get_attribute("href"))




# driver.close()
driver.quit()
