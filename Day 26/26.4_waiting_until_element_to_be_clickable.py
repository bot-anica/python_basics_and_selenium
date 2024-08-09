from time import sleep
from typing import List, Dict

import undetected_chromedriver as uc
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tabulate import tabulate

from selenium_methods import get_driver, get_page
from selenium_methods.core import scroll_mouse_wheel

# ---------- ОЖИДАНИЕ ПОКА ЭЛЕМЕНТ НЕ СТАНЕТ КЛИКАБЕЛЬНЫМ ИСПОЛЬЗУЯ SELENIUM
print("----- ОЖИДАНИЕ ПОКА ЭЛЕМЕНТ НЕ СТАНЕТ КЛИКАБЕЛЬНЫМ ИСПОЛЬЗУЯ SELENIUM -----")

# element_to_be_clickable - ожидание, пока элемент станет кликабельным

WEB_DRIVER_OPTIONS = ["--start-maximized", "--disable-popup-blocking"]
# URL = "https://comfy.ua/notebook/"
# URL = "https://www.temu.com/search_result.html?search_key=notebook&search_method=user"
URL = "https://hozsklad.ua/ua/tovary-dlya-doma-bytovaya-tekhnika-elektrochayniki"


def get_product_ids(driver: uc.Chrome) -> List[str]:
    """
    Формирование списка словарей с данными
    :param driver: uc.Chrome
    :return: List[Dict[str, str]]
    """
    data: List[str] = []
    all_product_wrappers = driver.find_elements(By.CSS_SELECTOR, "#products > div")

    for wrapper in all_product_wrappers:
        data.append(wrapper.get_attribute("id").split("-")[-1])

    return data


def get_pages_quantity(driver: uc.Chrome) -> int:
    """
    Определение количества страниц
    :param driver: uc.Chrome
    :return: int
    """
    products_per_page = 24
    products_quantity = int(driver.find_element(By.CSS_SELECTOR, ".products_shown").text.split(" ")[-1])

    # Pages quantity
    if products_quantity % products_per_page == 0:
        pages_quantity = products_quantity // products_per_page
    else:
        pages_quantity = products_quantity // products_per_page + 1

    return pages_quantity


def load_data(driver: uc.Chrome) -> None:
    """
    Нажатие кнопки "Показать ещё"
    :param driver: uc.Chrome
    :return: List[str]
    """
    current_page = 1
    pages_quantity = get_pages_quantity(driver)

    while current_page <= pages_quantity:
        try:
            if current_page < pages_quantity:
                element = (WebDriverWait(driver, 20).until(
                    # visibility_of_element_located - ожидание появления элемента, который станет видимым
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".next-page a"))
                ))
                element.click()

            sleep(0.5)
            current_page += 1
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
            continue
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
            continue
        except NoSuchElementException:
            print("NoSuchElementException")
            break
    else:
        print("All pages are loaded")
        print("Pages quantity: ", pages_quantity)


def select_language(driver: uc.Chrome) -> None:
    """
    Выбор языка
    :param driver: uc.Chrome
    :return: None
    """
    driver.find_element(By.CSS_SELECTOR, "#chooseLanguageSubmit").click()


def main() -> None:
    """
    Точка входа в программу
    :return: None
    """

    driver = get_driver(WEB_DRIVER_OPTIONS)
    get_page(URL, driver)

    select_language(driver)
    load_data(driver)

    sleep(3)


main()
