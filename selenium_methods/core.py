import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement


def get_driver(options: list) -> uc.Chrome:
    """
    Создание драйвера с настройками
    :param options: uc.ChromeOptions
    :return: uc.Chrome
    """

    if options:
        driver_options: uc.ChromeOptions = uc.ChromeOptions()

        for option in options:
            driver_options.add_argument(option)

        return uc.Chrome(options=driver_options)

    else:
        return uc.Chrome()


def get_page(url: str, driver: uc.Chrome) -> None:
    """
    Загрузка страницы
    :param url: str
    :param driver: uc.Chrome
    :return: None
    """

    driver.get(url)


def left_click(element: WebElement) -> None:
    """
    Нажатие левой кнопки мыши
    :param element: WebElement
    :return: None
    """
    element.click()


def right_click(element: WebElement, driver: uc.Chrome) -> None:
    """
    Нажатие правой кнопки мыши
    :param element: WebElement
    :param driver: uc.Chrome
    :return: None
    """
    webdriver.ActionChains(driver).context_click(element).perform()


def step_back(driver: uc.Chrome) -> None:
    """
    Возврат на предыдущую страницу
    :param driver: uc.Chrome
    :return: None
    """
    driver.back()


def step_forward(driver: uc.Chrome) -> None:
    """
    Переход на следующую страницу
    :param driver: uc.Chrome
    :return: None
    """
    driver.forward()


def get_refresh(driver: uc.Chrome) -> None:
    """
    Обновление страницы
    :param driver: uc.Chrome
    :return: None
    """
    driver.refresh()


def press_key(key: Keys, element: WebElement) -> None:
    """
    Нажатие клавиши
    :param key: Keys
    :param element: WebElement
    :return: None
    """
    element.send_keys(key)


def scroll_mouse_wheel(x: int, y: int, driver: uc.Chrome) -> None:
    """
    Прокрутка мыши
    :param x: int
    :param y: int
    :param driver: uc.Chrome
    :return: None
    """
    script = "window.scrollBy(%d, %d);" % (x, y)

    driver.execute_script(script)
