from time import sleep

from selenium import webdriver

# ---------- SELENIUM DRIVER
print("----- SELENIUM DRIVER -----")

# Применение библиотеки Selenium
# 1. Тестирование веб-приложений
# 2. Парсинг данных
# 3. Автоматизация веб-задач


# Основные опции в Selenium WebDriver

# 1. --headless: отключает отображение окна браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org")
sleep(5)

# 2. --window-size: задает размер окна браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=800x600")
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org")
sleep(5)

# 3. --disable-gpu: отключает использование GPU
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org")
sleep(5)

# 4. --start-maximized: разворачивает окно браузера на весь экран
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org")
sleep(5)


# Полноценный пример программы
options = webdriver.ChromeOptions()

# Установка дополнительных опции
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")

# Запуск браузера
driver = webdriver.Chrome(options=options)

driver.get("https://www.python.org")
# ... - код для тестирования

driver.close()
