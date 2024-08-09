from time import sleep
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

# ---------- SELENIUM BY CSS SELECTOR
print("----- SELENIUM BY CSS SELECTOR -----")

# Примеры CSS селекторов

# .class-name - CSS селектор для CSS-класса
# #element-id - CSS селектор для ID
# [attribute=value] - CSS селектор для атрибута
# :pseudo-class - CSS селектор для псевдокласса
# ::pseudo-element - CSS селектор для псевдоэлемента

BOOKS_URL = "http://books.toscrape.com/"
OLX_LOGIN_FORM_URL = r"https://login.olx.ua/?cc=eyJjYyI6MCwiZ3JvdXBzIjoiIn0%3D&client_id=309lsgh0deirlo2la9kmrmhe3v&code_challenge=97nk9HLOngWTCDOjfAsCi9aFLqqHl_JjdjcP8eeevaA&code_challenge_method=S256&lang=uk&redirect_uri=https%3A%2F%2Fwww.olx.ua%2Fd%2Fuk%2Fcallback%2F&st=eyJzbCI6IjE4YzIxYTAzMzI4eDU1NmFjODA3IiwicyI6IjE5MGM1MWU3NGM2eDZkZjYwOGQ4In0%3D&state=Z3NIOWtoZG9QeUJWNkdQdVE3SE95UGdQcWZCeDB2a0pIUUpncmVpdG03SQ%3D%3D"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(BOOKS_URL)

# Примеры поиска элементов по CSS селектору

# Найти "article" с классом ".product_pod"
first_product_pod: WebElement = driver.find_element(By.CSS_SELECTOR, "article.product_pod")
print(first_product_pod.text)

# Найти элемент с id "username"
promotions_left: WebElement = driver.find_element(By.CSS_SELECTOR, "#promotions_left")
print(promotions_left.text)

# Найти ссылки, содержащие атрибут rel="nofollow"
links_with_nofollow: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, "a[rel='nofollow']")
print(len(links_with_nofollow))

# Найти первый дочерний элемент списка
first_ul_child: WebElement = driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-list ul > li:first-child")
print(first_ul_child.text)

# Найти полные названия книг (h3 a title)
product_cards: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, ".product_pod")

for card in product_cards:
    link: WebElement = card.find_element(By.CSS_SELECTOR, "h3 a")
    book_title = link.get_attribute("title")
    print(book_title)

