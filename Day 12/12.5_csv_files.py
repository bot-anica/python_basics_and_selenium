import csv
from pprint import pprint

# ---------- CSV FILES
print("----- CSV FILES -----")

# Пример данных в CSV формате:
# name,age,grades
# John,25,88
# Alice,22,100
# Bob,30,80
# Сергей,25,88

# По умолчанию CSV файлы имеют кодировку WINDOWS-1251
# и в качестве разделителя полей используются запятые.

# Чтение и запись в CSV файл

students = [
    ["Имя", "Возраст", "Средняя оценка"],
    ["Сергей", "25", "88"],
    ["Алиса", "22", "100"],
    ["Боб", "30", "80"],
    ["Виктория", "25", "88"],
]


# Записать данные в CSV файл
with open("students.csv", "w", encoding="windows-1251", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(students)


# Чтение данных из CSV файл
with open("students.csv", "r", encoding="windows-1251", newline='') as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)
    pprint(data)


# Добавить новую строку
with open("students.csv", "a", encoding="windows-1251", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Виктория", "25", "88"])


# Работа с данными CSV в виде словарей
# Для этого используется DictWriter и DictReader

fieldnames = ["name", "age", "grades"]

students = [
    {"name": "Сергей", "age": "25", "grades": "88"},
    {"name": "Алиса", "age": "22", "grades": "100"},
    {"name": "Боб", "age": "30", "grades": "80"},
    {"name": "Виктория", "age": "25", "grades": "88"},
]

# DictWriter: Запись данных в CSV файл
with open("students.csv", "w", encoding="windows-1251", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(students)


# DictReader: Чтение данных из CSV файл
with open("students.csv", "r", encoding="windows-1251", newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)
    pprint(data)


# DictWriter: Добавление новой строки
with open("students.csv", "a", encoding="windows-1251", newline='') as file:
    new_row = {"name": "Виктория", "age": "25", "grades": "88"}
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writerow(new_row)
    file.close()
