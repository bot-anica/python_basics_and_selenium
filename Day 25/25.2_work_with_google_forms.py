from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_methods import get_driver, get_page, get_form, get_form_fields, get_usual_input, get_radio_button, \
    get_radio_buttons, get_checkboxes, get_selector, get_selector_options, get_datepicker, get_submit_button, \
    get_checkbox

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
    get_page("https://docs.google.com/forms/d/e/1FAIpQLSfP0lcoj1XrdXtKCSwSkCaPEgGaGkY267U6yLCH3WkIz-58vg/viewform?usp=sf_link", driver)

    # Создание новой вкладки
    driver.execute_script('''document.querySelector("form").addEventListener("submit",(function(e){var o=new FormData(form);for(var t of(console.log(Object.fromEntries(o)),o.entries()))console.log(t[0]+": "+t[1])}));''')
    # driver.execute_script('''document.querySelector("form").addEventListener("click",(function(e){console.log(e.target);}));''')

    form = get_form(driver)

    form_fields = get_form_fields(form)

    first_name_input = get_usual_input(form_fields[0])
    last_name_input = get_usual_input(form_fields[1])
    job_title_input = get_usual_input(form_fields[2])

    radio_buttons = get_radio_buttons(form_fields[3])

    radio_button_1 = get_radio_button(radio_buttons[0])
    radio_button_2 = get_radio_button(radio_buttons[1])
    radio_button_3 = get_radio_button(radio_buttons[2])

    checkboxes = get_checkboxes(form_fields[4])

    checkbox_1 = get_checkbox(checkboxes[0])
    checkbox_2 = get_checkbox(checkboxes[1])
    checkbox_3 = get_checkbox(checkboxes[2])
    checkbox_4 = get_checkbox(checkboxes[3])
    checkbox_5 = get_checkbox(checkboxes[4])

    selector = get_selector(form_fields[5])

    datepicker = get_datepicker(form_fields[6])

    submit_button = get_submit_button(form)

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    job_title_input.send_keys("Software Developer")
    radio_button_2.click()
    checkbox_1.click()
    checkbox_3.click()

    selector.click()

    sleep(0.5)

    selector_options = get_selector_options(selector)
    selector_options[4].click()

    datepicker.send_keys("01/01/2023")

    submit_button.click()

    sleep(50)


main()
