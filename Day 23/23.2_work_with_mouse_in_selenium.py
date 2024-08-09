# ---------- РАБОТА С КЛАВИАТУРОЙ
from time import sleep

import undetected_chromedriver as uc
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium_methods import scroll_mouse_wheel, get_driver, get_page

print("----- РАБОТА С КЛАВИАТУРОЙ -----")

WEB_DRIVER_OPTIONS = ["--start-maximized"]
FORM_URL = "https://demo.seleniumeasy.com/basic-first-form-demo.html"
IMAGES_URL = "https://stockcake.com/"
URL = "https://dns-shop.ru/catalog/17a8943716404e77/monitory"


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
    # vpn_crx_file = get_vpn_crx_file()
    # install_extension("BIHMPLHOBCHOAGEEOKMGBDIHKNKJBKND_5_0_18_0.crx", driver)
    get_page(URL, driver)

    sleep(2)

    dns_scroll_more_button(driver)

    # # Обычное нажатие кнопкой мыши (левой кнопкой)
    # driver.find_element(By.CSS_SELECTOR, ".masonry-grid article a").click()
    #
    # sleep(5)
    #
    # # Нажатие правой кнопки мыши
    # image: WebElement = driver.find_element(By.CSS_SELECTOR, "picture img")
    # action = webdriver.ActionChains(driver)
    # action.context_click(image).perform()

    sleep(150)


main()
