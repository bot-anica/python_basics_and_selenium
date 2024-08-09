from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# ---------- ТИПИЗАЦИЯ ДЛЯ БИБЛИОТЕКИ SELENIUM
print("----- ТИПИЗАЦИЯ ДЛЯ БИБЛИОТЕКИ SELENIUM -----")


def find_element_by_id(driver: webdriver, id: str) -> WebElement:
    return driver.find_element(By.ID, id)


driver = webdriver.Chrome()
element = find_element_by_id(driver, "#username")


def find_elements_by_class_name(driver: webdriver, selector: str) -> List[WebElement]:
    return driver.find_elements(By.CSS_SELECTOR, selector)


elements = find_elements_by_class_name(driver, "ul > li")
