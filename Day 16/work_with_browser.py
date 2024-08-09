# ---------- МОДУЛИ И ПАКЕТЫ

# Модуль - это файл с расширением .py
# Пакет - это каталог с файлами .py

# Допустим это модуль для работы с автоматизацией браузера

def open_browser(browser_name):
    print(f"Opening {browser_name} browser")
    pass


def close_browser(browser_name):
    print(f"Closing {browser_name} browser")
    pass


def parse_page(url):
    print(f"Parsing {url}")
    pass


def parse_site(url):
    open_browser("Chrome")
    parse_page(url)
    close_browser("Chrome")