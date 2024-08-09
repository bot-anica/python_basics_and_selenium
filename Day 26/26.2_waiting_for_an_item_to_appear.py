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

# ---------- ОЖИДАНИЕ ПОЯВЛЕНИЯ ЭЛЕМЕНТА ИСПОЛЬЗУЯ SELENIUM
print("----- ОЖИДАНИЕ ПОЯВЛЕНИЯ ЭЛЕМЕНТА ИСПОЛЬЗУЯ SELENIUM -----")

# presence_of_element_located - ожидание появления элемента

# Ожидание появления элемента до тех пор, пока следующая строка кода не станет доступной для выполнения

WEB_DRIVER_OPTIONS = ["--start-maximized", "--disable-popup-blocking"]
# URL = "https://comfy.ua/notebook/"
# URL = "https://www.temu.com/search_result.html?search_key=notebook&search_method=user"
URL = "https://hozsklad.ua/ua/tovary-dlya-doma-bytovaya-tekhnika-elektrochayniki"


def get_data(driver: uc.Chrome) -> List[Dict[str, str]]:
    """
    Формирование списка словарей с данными
    :param driver: uc.Chrome
    :return: List[Dict[str, str]]
    """
    data: List[Dict[str, str]] = []
    all_product_wrappers = driver.find_elements(By.CSS_SELECTOR, "#products > div")

    for wrapper in all_product_wrappers:
        url = wrapper.find_element(By.CSS_SELECTOR, ".product_card__img_wrapper a").get_attribute("href")
        title = wrapper.find_element(By.CSS_SELECTOR, ".product_card__title").text
        price = wrapper.find_element(By.CSS_SELECTOR, ".product_card__price").text
        image_url = (
            wrapper.find_element(By.CSS_SELECTOR, ".product_card__img_wrapper a > img").get_attribute("src"))

        data.append({"title": title, "price": price, "url": url, "image_url": image_url})

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
    :return: None
    """
    current_page = 1
    pages_quantity = get_pages_quantity(driver)

    while current_page < pages_quantity:
        try:
            scroll_mouse_wheel(0, 2000, driver)
            element = (WebDriverWait(driver, 20).until(
                # presence_of_element_located - ожидание появления элемента в DOM-дереве
                EC.presence_of_element_located((By.CSS_SELECTOR, ".category__show_more_btn"))
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

    products = get_data(driver)

    table = tabulate(products, headers="keys", tablefmt="github")

    print(table)
    print(f"Всего продуктов: {len(products)}")


main()
