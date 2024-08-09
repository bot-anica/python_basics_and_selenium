# ---------- РАБОТА С МЫШЬЮ
from time import sleep

import undetected_chromedriver as uc
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium_methods import get_driver, get_page, scroll_mouse_wheel, press_key

print("----- РАБОТА С МЫШЬЮ -----")

WEB_DRIVER_OPTIONS = ["--start-maximized"]
FORM_URL = "https://demo.seleniumeasy.com/basic-first-form-demo.html"
IMAGES_URL = "https://stockcake.com/"
URL = "https://dns-shop.ru"



def dns_scroll_more_button(driver: uc.Chrome) -> None:
    """
    Нажатие кнопки "Показать ещё"
    :param driver: uc.Chrome
    :return: None
    """
    while True:
        try:
            scroll_mouse_wheel(0, 2000, driver)
            driver.find_element(By.CSS_SELECTOR, "#products-list-pagination > button").click()
            sleep(1)
        except NoSuchElementException:
            scroll_mouse_wheel(0, 2000, driver)
            break


def main() -> None:
    """
    Точка входа в программу
    :return: None
    """

    driver: uc.Chrome = get_driver(WEB_DRIVER_OPTIONS)
    get_page(URL, driver)

    sleep(2)

    search_field = driver.find_element(By.CSS_SELECTOR, "input[name=q]")
    search_field.send_keys("monitor")
    press_key(Keys.ENTER, search_field)

    sleep(2)

    dns_scroll_more_button(driver)

    sleep(150)


main()

