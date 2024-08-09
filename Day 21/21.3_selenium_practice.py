from pprint import pprint
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from tabulate import tabulate

# ---------- SELENIUM ПРАКТИКА
print("----- SELENIUM ПРАКТИКА -----")

# Задание

# 1. Сохранить данные книг со всех страниц
# 2. Отобразить эти данные в таблице

TARGET_URL = "http://books.toscrape.com/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get(TARGET_URL)


def get_pages_text() -> str:
    """
    :return: текст, в котором указан номер актуальной страницы и количество страниц
    """
    global driver
    pages_text_element = driver.find_element(By.CSS_SELECTOR, ".pager > .current")
    return pages_text_element.text


def get_pages_quantity(text: str) -> int:
    """
    :param text: текс о номере страницы и количестве страниц
    :return: количество страниц
    """
    return int(text.split(" ")[-1])


def get_book_elements() -> List[WebElement]:
    """
    :return: элементы книг на странице
    """
    return driver.find_elements(By.CSS_SELECTOR, ".product_pod")


def get_book_image_url(element: WebElement) -> str:
    """
    :param element: элемент одной книги
    :return: ссылка на изображение данной книги
    """
    image_element: WebElement = element.find_element(By.CSS_SELECTOR, ".thumbnail")
    return image_element.get_attribute("src")


def get_book_title(element: WebElement) -> str:
    """
    :param element: элемент одной книги
    :return: Название книги
    """
    link: WebElement = element.find_element(By.CSS_SELECTOR, "h3 > a")
    return link.get_attribute("title")


def get_book_price_element(element: WebElement) -> WebElement:
    """
    :param element: элемент одной книги
    :return: элемент блока цены книги
    """
    return element.find_element(By.CSS_SELECTOR, ".product_price")


def get_book_price(element: WebElement) -> str:
    """
    :param element: элемент блока цены книги
    :return: цена книги
    """
    return element.find_element(By.CSS_SELECTOR, ".price_color").text


def check_if_book_in_store(element: WebElement) -> bool:
    """
    :param element: элемент блока цены книги
    :return: есть ли книга в магазине
    """
    book_is_in_stock: int = (element.find_element(By.CSS_SELECTOR, ".availability")
                             .get_attribute("class")
                             .find("instock"))

    if book_is_in_stock == -1:
        return False
    else:
        return True


def process_book_element(element: WebElement) -> Dict[str, str]:
    """
    :param element: элемент одной книги
    :return: словарь книги
    """

    book_image_url: str = get_book_image_url(element)
    book_link_title: str = get_book_title(element)

    book_price_element: WebElement = get_book_price_element(element)
    book_price: str = get_book_price(book_price_element)
    book_is_in_stock: bool = check_if_book_in_store(book_price_element)

    return {
        "image_url": book_image_url,
        "title": book_link_title,
        "price": book_price,
        "in_stock": book_is_in_stock
    }


def click_next_page() -> None:
    next_page_link_element: WebElement = driver.find_element(By.CSS_SELECTOR, "ul.pager li.next a")
    next_page_link_element.click()


def main():
    books: List[Dict[str, str]] = []

    pages_text: str = get_pages_text()
    pages_quantity: int = get_pages_quantity(pages_text)

    while pages_quantity > 0:
        book_elements: List[WebElement] = get_book_elements()

        for book_element in book_elements:
            book: Dict[str, str] = process_book_element(book_element)
            books.append(book)

        pages_quantity -= 1

        if pages_quantity > 0:
            click_next_page()

    table = tabulate(books, headers="keys", tablefmt="pgql")
    print(table)


main()
