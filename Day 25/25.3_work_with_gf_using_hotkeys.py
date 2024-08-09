from time import sleep
from typing import List

from python_selenium_google_form import FieldConfig, FieldType, process_form_fields_with_hotkeys

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
    driver.implicitly_wait(10)

    get_page(
        "https://docs.google.com/forms/d/e/1FAIpQLSfP0lcoj1XrdXtKCSwSkCaPEgGaGkY267U6yLCH3WkIz-58vg/viewform?usp=sf_link",
        driver)

    # Создание новой вкладки
    driver.execute_script(
        '''document.querySelector("form").addEventListener("submit",(function(e){var o=new FormData(form);for(var t of(console.log(Object.fromEntries(o)),o.entries()))console.log(t[0]+": "+t[1])}));''')
    # driver.execute_script('''document.querySelector("form").addEventListener("click",(function(e){console.log(e.target);}));''')

    fields_list: List[FieldConfig] = [
        FieldConfig("first_name", FieldType.TEXT, "John"),
        FieldConfig("last_name", FieldType.TEXT, "Doe"),
        FieldConfig("job_title", FieldType.TEXT, "Software Developer"),
        FieldConfig("education_level", FieldType.RADIO, [1, 0, 0]),
        FieldConfig("favourite_subjects", FieldType.CHECKBOX, [0, 0, 1, 1, 0]),
        FieldConfig("experience", FieldType.SELECT, [0, 0, 1, 0]),
        FieldConfig("date", FieldType.DATE, "01-09-2022"),
    ]

    process_form_fields_with_hotkeys(fields_list, driver)

    sleep(10)


main()
