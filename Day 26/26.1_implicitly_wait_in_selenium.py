from selenium.webdriver.common.by import By

from selenium_methods import get_driver, get_page

# ---------- НЕЯВНОЕ ОЖИДАНИЕ В SELENIUM
print("----- НЕЯВНОЕ ОЖИДАНИЕ В SELENIUM -----")

# implicitly_wait - неявное ожидание

# Неявное ожидание выполняется до тех пор, пока следующая строка кода не станет доступной для выполнения

# Оно указывается в начале скрипта
# Если каждая следующая строка кода получает возможность выполниться раньше,
# то оно выполняется, а ожидание начинает новый отсчёт для следующей строки кода
# Если неявное ожидание не выполнится, то будет ошибка

WEB_DRIVER_OPTIONS = ["--start-maximized", "--disable-popup-blocking"]

driver = get_driver(WEB_DRIVER_OPTIONS)
driver.implicitly_wait(5)  # устанавливает неявное ожидание в 5 секунд

get_page("https://the-internet.herokuapp.com/dynamic_loading/1", driver)

driver.find_element(By.CSS_SELECTOR, "div#start > button").click()
driver.find_element(By.CSS_SELECTOR, "div#finish").click()
