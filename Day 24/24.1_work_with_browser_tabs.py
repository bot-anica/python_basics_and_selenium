# ---------- РАБОТА С ВКЛАДКАМИ БРАУЗЕРА В Python Selenium Chrome
from time import sleep
from typing import List

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_methods import get_driver, get_page

print("----- РАБОТА С ВКЛАДКАМИ БРАУЗЕРА В Python Selenium Chrome -----")

WEB_DRIVER_OPTIONS = ["--start-maximized", "--disable-popup-blocking"]

# Получение списка вкладок и их заголовков
# Используем метод driver.window_handles
# Используем метод driver.title

# Для переключения на вкладку используем метод driver.switch_to.window(handle)


def main() -> None:
    """
    Точка входа в программу
    :return: None
    """
    driver = get_driver(WEB_DRIVER_OPTIONS)
    get_page("https://google.com", driver)

    # Создание новой вкладки
    driver.execute_script('''window.open("http://bings.com","_blank");''')

    # Список вкладок
    tabs: List[str] = driver.window_handles

    # Заголовки вкладок
    tab_titles: List[str] = []

    for tab in tabs:
        driver.switch_to.window(tab)
        tab_titles.append(driver.title)

    print(tab_titles)

    sleep(5)

    # Закрываем вкладку
    driver.switch_to.window(tabs[-1])
    driver.close()

    sleep(5)


main()
