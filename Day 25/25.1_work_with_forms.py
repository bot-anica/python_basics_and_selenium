from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_methods import get_driver, get_page

# ---------- РАБОТА С ФОРМАМИ ИСПОЛЬЗУЯ SELENIUM
print("----- РАБОТА С ФОРМАМИ ИСПОЛЬЗУЯ SELENIUM -----")


WEB_DRIVER_OPTIONS = ["--start-maximized", "--disable-popup-blocking"]

def main() -> None:
    """
    Точка входа в программу
    :return: None
    """
    driver = get_driver(WEB_DRIVER_OPTIONS)
    get_page("https://formy-project.herokuapp.com/form", driver)

    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    job_title_input = driver.find_element(By.ID, "job-title")
    radio_button_1 = driver.find_element(By.ID, "radio-button-1")
    radio_button_2 = driver.find_element(By.ID, "radio-button-2")
    radio_button_3 = driver.find_element(By.ID, "radio-button-3")
    checkbox_1 = driver.find_element(By.ID, "checkbox-1")
    checkbox_2 = driver.find_element(By.ID, "checkbox-2")
    checkbox_3 = driver.find_element(By.ID, "checkbox-3")
    selector = driver.find_element(By.ID, "select-menu")
    datepicker = driver.find_element(By.ID, "datepicker")

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    job_title_input.send_keys("Software Developer")
    radio_button_2.click()
    checkbox_1.click()
    checkbox_3.click()
    selector.click()
    selector.send_keys(Keys.ARROW_DOWN)
    selector.send_keys(Keys.ARROW_DOWN)
    selector.send_keys(Keys.RETURN)
    datepicker.send_keys("01/01/2023")

    submit_button.click()

    sleep(50)

main()

