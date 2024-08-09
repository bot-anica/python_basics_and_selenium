# ---------- ПРИМЕРЫ ИЗВЛЕЧЕНИЯ ДАННЫХ ИСПОЛЬЗУЯ Selenium
import csv
import json
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

print("----- ПРИМЕРЫ ИЗВЛЕЧЕНИЯ ДАННЫХ ИСПОЛЬЗУЯ Selenium -----")

WEB_DRIVER_OPTIONS = ["--headless"]
SITE_URL = "https://getbootstrap.com/docs/4.0/content/tables/"
# SITE_URL = "http://books.toscrape.com/"

def get_driver(options: list = WEB_DRIVER_OPTIONS) -> webdriver.Chrome:
    """
    Создание драйвера с настройками
    :param options: webdriver.ChromeOptions
    :return: webdriver.Chrome
    """

    if options:
        driver_options: webdriver.ChromeOptions = webdriver.ChromeOptions()

        for option in options:
            driver_options.add_argument(option)

        return webdriver.Chrome(options=driver_options)

    else:
        return webdriver.Chrome()


def get_page(url: str, driver: webdriver.Chrome) -> None:
    """
    Загрузка страницы
    :param url: str
    :param driver: webdriver.Chrome
    :return: None
    """

    driver.get(url)


# def main() -> None:
#     """
#     Точка входа в программу
#     :return: None
#     """
#
#     driver: webdriver.Chrome = get_driver()
#     get_page(SITE_URL, driver)
#
#     results: List[Dict[str, str]] = []
#
#     product_pods = driver.find_elements(By.CSS_SELECTOR, ".product_pod")
#
#     for product_pod in product_pods:
#         title = product_pod.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#         url = product_pod.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href")
#         image_url = product_pod.find_element(By.CSS_SELECTOR, "img.thumbnail").get_attribute("src")
#         price = product_pod.find_element(By.CSS_SELECTOR, ".price_color").text
#
#         results.append({
#             "title": title,
#             "url": url,
#             "image_url": image_url,
#             "price": price
#         })
#
#     with open("books.json", "w", encoding="utf8") as file:
#         json.dump(results, file, indent=4, ensure_ascii=False)
#
#     with open("books.csv", "w", encoding="utf8") as file:
#         writer = csv.DictWriter(file, fieldnames=results[0].keys(), delimiter=";")
#         writer.writeheader()
#         writer.writerows(results)


def main() -> None:
    """
    Точка входа в программу
    :return: None
    """

    driver: webdriver.Chrome = get_driver()
    get_page(SITE_URL, driver)

    # Получаем таблицу
    table = driver.find_element(By.CSS_SELECTOR, "table")

    # Из thead получаем её заголовки
    headers: List[WebElement] = table.find_elements(By.CSS_SELECTOR, "thead th")
    headers_results: List[str] = []
    for header in headers:
        headers_results.append(header.text)

    # Из tbody получаем её строки
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    results: List[Dict[str, str]] = []

    # Перебираем все строки в tbody и добавляем их в словарь
    for row_index, row in enumerate(rows):
        row_results: Dict[str, str] = {}

        cells = row.find_elements(By.TAG_NAME, "td")

        for cell_index, cell in enumerate(cells):
            row_results[headers[cell_index].text] = cell.text

        results.append(row_results)

    # Записываем в CSV
    with open("users.csv", "w", encoding="windows-1251", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers_results, delimiter=";")
        writer.writeheader()
        writer.writerows(results)

main()
