from pprint import pprint

from selenium import webdriver
from art import text2art
import csv
from tabulate import tabulate
from plyer import notification

# ---------- Библиотеки ----------
print("----- LIBRARIES -----")

# Библиотека Selenium
# browser = webdriver.Chrome()
# browser.get("https://www.python.org")


# Библиотека art
print(text2art("Python"))


# Библиотека Tabulate
with open("students.csv", "r", encoding="windows-1251", newline='') as file:
    reader = csv.reader(file, delimiter=';')
    students_data_lists = list(reader)  # Данные в формате массива массивов

with open("students.csv", "r", encoding="windows-1251", newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    students_data_dicts = list(reader)  # Данные в формате массива словарей

# Отображаем в таблице массив массивов
print("\nОтображаем в таблице массив массивов")
pprint(students_data_lists)
table = tabulate(students_data_lists, headers="firstrow", tablefmt="pretty")
print(table)

# Отображаем в таблице массив словарей
print("\nОтображаем в таблице массив словарей")
pprint(students_data_dicts)
table = tabulate(students_data_dicts, headers="keys", tablefmt="pretty")
print(table)


# Библиотека Plyer для отображения уведомлений в системе
notification.notify(
    title="Python Plyer",
    message="Библиотека Plyer для отображения уведомлений в системе",
    timeout=10
)
