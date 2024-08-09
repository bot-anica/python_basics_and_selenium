from enum import Enum
from time import sleep
from typing import List, Union

import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


path_to_usual_input = "input"
path_to_radio_buttons = "label"
path_to_radio_button = "div > div:nth-child(1) > div"
path_to_checkboxes = "label"
path_to_checkbox = "div > div:nth-child(1)"
path_to_selector = "div > div > div:nth-child(2) > div"
path_to_selector_options = "div:nth-child(2) > div"


def get_form(driver: uc.Chrome) -> WebElement:
    return driver.find_element(By.TAG_NAME, "form")


def get_form_fields(form: WebElement) -> List[WebElement]:
    return form.find_elements(By.CSS_SELECTOR, "div:nth-child(2) > div > div:nth-child(2) > div[role=listitem]")


def get_usual_input(form_field: WebElement) -> WebElement:
    return form_field.find_element(By.CSS_SELECTOR, path_to_usual_input)


def get_radio_buttons(form_field: WebElement) -> List[WebElement]:
    return form_field.find_elements(By.CSS_SELECTOR, path_to_radio_buttons)


def get_radio_button(radio_button_wrapper: WebElement) -> WebElement:
    return radio_button_wrapper.find_element(By.CSS_SELECTOR, path_to_radio_button)


def get_checkboxes(form_field: WebElement) -> List[WebElement]:
    return form_field.find_elements(By.CSS_SELECTOR, path_to_checkboxes)


def get_checkbox(checkbox_wrapper: WebElement) -> WebElement:
    return checkbox_wrapper.find_element(By.CSS_SELECTOR, path_to_checkbox)


def get_selector(form_field: WebElement) -> WebElement:
    return form_field.find_element(By.CSS_SELECTOR, path_to_selector)


def get_selector_options(selector: WebElement) -> List[WebElement]:
    return selector.find_elements(By.CSS_SELECTOR, path_to_selector_options)


def get_datepicker(form_field: WebElement) -> WebElement:
    return form_field.find_element(By.CSS_SELECTOR, path_to_usual_input)


def get_submit_button(form: WebElement) -> WebElement:
    return form.find_element(By.CSS_SELECTOR, "[role=button]")


class FieldType(Enum):
    TEXT = "text"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"
    DATE = "date"


class FieldConfig:
    def __init__(self, key: str, type: FieldType, value: Union[str, List[int]]):
        self.key = key
        self.type = type
        self.value = value


def get_active_element(driver: uc.Chrome) -> WebElement:
    return driver.switch_to.active_element


def process_text_field(value: str, driver: uc.Chrome) -> None:
    active_field = get_active_element(driver)
    active_field.send_keys(value)


def process_radio_buttons_field(value: List[int], driver: uc.Chrome) -> None:
    active_field = get_active_element(driver)

    for index, option_value in enumerate(value):
        if option_value == 1:
            if index == 0:
                active_field.send_keys(Keys.ARROW_DOWN)
                active_field = get_active_element(driver)
                active_field.send_keys(Keys.ARROW_UP)
        else:
            active_field.send_keys(Keys.ARROW_DOWN)

        if option_value == 1:
            active_field = get_active_element(driver)
            active_field.send_keys(Keys.TAB)
            break


def process_checkbox_field(value: List[int], driver: uc.Chrome) -> None:
    variants_quantity = len(value)

    for index, option_value in enumerate(value):
        if option_value == 1:
            active_field = get_active_element(driver)
            active_field.send_keys(Keys.SPACE)

        if index < variants_quantity - 1:
            active_field = get_active_element(driver)
            active_field.send_keys(Keys.TAB)


def process_select_field(value: List[int], driver: uc.Chrome) -> None:
    active_field = get_active_element(driver)
    variants_quantity = len(value)

    active_field.send_keys(Keys.SPACE)
    active_field.send_keys(Keys.ARROW_DOWN)
    sleep(0.5)

    for index, option_value in enumerate(value):
        active_field = get_active_element(driver)

        if option_value == 1:
            active_field.send_keys(Keys.SPACE)
            break

        if index < variants_quantity - 1:
            active_field.send_keys(Keys.ARROW_DOWN)
            sleep(0.5)


def process_date_field(value: str, driver: uc.Chrome) -> None:
    active_field = get_active_element(driver)
    active_field.send_keys(value)


# def process_range_field(value: str, driver: uc.Chrome) -> None:
#     active_field = get_active_element(driver)
#     sleep(0.1)
#     driver.execute_script(f"arguments[0].value = {value}", active_field)


def process_form_fields_with_hotkeys(fields_list: List[FieldConfig], driver: uc.Chrome) -> None:
    body = get_active_element(driver)

    body.send_keys(Keys.TAB)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.TAB)

    for field_config in fields_list:
        if field_config.type == FieldType.TEXT:
            process_text_field(field_config.value, driver)
        elif field_config.type == FieldType.RADIO:
            process_radio_buttons_field(field_config.value, driver)
        elif field_config.type == FieldType.CHECKBOX:
            process_checkbox_field(field_config.value, driver)
        elif field_config.type == FieldType.SELECT:
            process_select_field(field_config.value, driver)
        elif field_config.type == FieldType.DATE:
            process_date_field(field_config.value, driver)

        active_field = get_active_element(driver)
        sleep(0.1)
        active_field.send_keys(Keys.TAB)
        sleep(0.1)

    submit_button = get_active_element(driver)

    submit_button.click()
