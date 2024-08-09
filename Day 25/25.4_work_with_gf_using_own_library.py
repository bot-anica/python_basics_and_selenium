from time import sleep
from typing import List

from selenium_methods import get_driver, get_page, get_form, get_form_fields, get_usual_input
from selenium_methods.google_form import process_form_fields_with_hotkeys, FieldConfig, FieldType

# ---------- РАБОТА С ФОРМАМИ ИСПОЛЬЗУЯ SELENIUM
print("----- РАБОТА С ФОРМАМИ ИСПОЛЬЗУЯ SELENIUM -----")

'''
JS Script:

function submitForm(formId) {
    const form = document.getElementById(formId);
    const formData = new FormData(form);

    const formObject = {};
    for (const [key, value] of formData.entries()) {
        formObject[key] = value;
    }

    const successMessageWrapper = document.querySelector('.alert.alert-success');
    successMessageWrapper.textContent = `The form was successfully submitted!\n\n${JSON.stringify(formObject)}`;
}
'''

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
