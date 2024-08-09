from time import sleep
from typing import List

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

# ---------- SELENIUM WEBDRIVER И ИНСТРУМЕНТ BY
print("----- SELENIUM WEBDRIVER И ИНСТРУМЕНТ BY -----")

# Selenium WebDriver - библиотека для работы с браузером.

# Инструмент By - библиотека для работы с элементами страницы
# с помощью языка программирования Python.

# find_element() - возвращает первый элемент, соответствующий заданному критерию поиска
# find_elements() - возвращает список элементов, соответствующих заданному критерию поиска

# Способы поиска элементов веб-страницы используя инструмент By

# 1. ID - идентификатор элемента
# 2. NAME - имя элемента
# 3. CLASS_NAME - имя CSS-класса
# 4. TAG_NAME - имя тега
# 5. LINK_TEXT - текст ссылки
# 6. PARTIAL_LINK_TEXT - частичное совпадение текста ссылки
# 7. XPATH - путь XPath
# 8. CSS_SELECTOR - селектор CSS

BOOKS_URL = "http://books.toscrape.com/"
OLX_LOGIN_FORM_URL = r"https://login.olx.ua/?cc=eyJjYyI6MCwiZ3JvdXBzIjoiIn0%3D&client_id=309lsgh0deirlo2la9kmrmhe3v&code_challenge=97nk9HLOngWTCDOjfAsCi9aFLqqHl_JjdjcP8eeevaA&code_challenge_method=S256&lang=uk&redirect_uri=https%3A%2F%2Fwww.olx.ua%2Fd%2Fuk%2Fcallback%2F&st=eyJzbCI6IjE4YzIxYTAzMzI4eDU1NmFjODA3IiwicyI6IjE5MGM1MWU3NGM2eDZkZjYwOGQ4In0%3D&state=Z3NIOWtoZG9QeUJWNkdQdVE3SE95UGdQcWZCeDB2a0pIUUpncmVpdG03SQ%3D%3D"

# Создаём объект настроек
options = webdriver.ChromeOptions()

# Добавляем настройки
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")

# Запускаем браузер
driver = webdriver.Chrome(options=options)

# Переходим на страницу
driver.get(BOOKS_URL)


# # Ищем первый элемент (driver.find_element) по названию класса (By.CLASS_NAME)
# print("\nИщем первый элемент (driver.find_element) по названию класса (By.CLASS_NAME)\n")
# first_alert_warning_element: WebElement = driver.find_element(By.CLASS_NAME, "alert-warning")
#
# print(first_alert_warning_element.text)
# print("\n" + "--" * 10)
#
#
# # Ищем все элементы (driver.find_elements) по названию класса (By.CLASS_NAME)
# print("\nИщем все элементы (driver.find_elements) по названию класса (By.CLASS_NAME)\n")
# product_pods: List[WebElement] = driver.find_elements(By.CLASS_NAME, "product_pod")
#
# for item in product_pods:
#     print(item.text + "\n")
#
# print("\n" + "--" * 10)
#
#
# # Ищем элементы по тегу (By.TAG_NAME)
# print("\nИщем элементы по тегу (By.TAG_NAME)\n")
#
# for item in product_pods:
#     header_level_2: WebElement = item.find_element(By.TAG_NAME, "h3")
#     print(header_level_2.text)
#
# print("\n" + "--" * 10)
#
#
# Ищем элементы по тегу (By.NAME)
# print("\nИщем элементы по тегу (By.NAME)\n")
# driver.get(OLX_LOGIN_FORM_URL)
#
# username_input: WebElement = driver.find_element(By.NAME, "username")
# password_input: WebElement = driver.find_element(By.NAME, "password")
# username_input.send_keys("test@gmail.com")
# password_input.send_keys("qwerasd123")
# password_input.send_keys(Keys.ENTER)
#
# sleep(5)


# Ищем элементы по тексту (By.LINK_TEXT)
print("\nИщем элементы по тексту (By.LINK_TEXT)\n")
driver.get(BOOKS_URL)

product_pod_link: WebElement = driver.find_element(By.LINK_TEXT, "A Light in the ...")
product_pod_link.click()

sleep(5)

# Возвращаемся назад
driver.back()
sleep(2)

# Ищем элементы по части текста (By.PARTIAL_LINK_TEXT)
print("\nИщем элементы по части текста (By.PARTIAL_LINK_TEXT)\n")

product_pod_link: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, "Light in the")
product_pod_link.click()

sleep(5)

