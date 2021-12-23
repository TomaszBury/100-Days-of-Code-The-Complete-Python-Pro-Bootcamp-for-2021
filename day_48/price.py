from selenium.webdriver.common.by import By


def can_i_buy(what, driver):
    grandma_class = driver.find_element(By.ID, value=what)
    if grandma_class.get_attribute('class') == 'grayed':
        return False
    return True


def price_of_grandma(driver):
    grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")

    return grandma.text.split(" ")[2]
