import json
from pprint import pprint

# ---------- JSON FILE
print("----- JSON FILE -----")

# JSON - JavaScript Object Notation

# Основные методы работы с JSON:

# dump - записывает данные в файл
# dumps - преобразует строку в JSON
# load - считывает JSON файл
# loads - считывает JSON текст, например, из сети


students = [
    {"name": "John", "age": 25, "grades": [88, 76, 92], "got_a": True},
    {"name": "Alice", "age": 22, "grades": [100, 100, 100], "got_a": True},
    {"name": "Bob", "age": 30, "grades": [80, 70, 90], "got_a": False}
]


# -------------------------------------------------------
# dump - записывает данные в файл
with open("students.json", "w") as file:
    json.dump(students, indent=4, ensure_ascii=False, fp=file)


# -------------------------------------------------------
# dumps - преобразует строку в JSON
students_json = json.dumps(students, indent=4, ensure_ascii=False)  # dumps - преобразует формат Python в JSON

with open("students.json", "w") as file:
    file.write(students_json)


# -------------------------------------------------------
# load - считывает JSON файл
with open("students.json", "r") as file:
    data = json.load(file)  # load - считывает JSON файл
    print(data)


# -------------------------------------------------------
# loads - считывает JSON текст, например, из сети
students_list = json.loads(students_json)  # loads - преобразует JSON в Python
print(students_list)

students_list.append({"name": "Сергей", "age": 25, "grades": [88, 76, 92], "got_a": True})

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students_list, indent=4, ensure_ascii=False, fp=file)


# -------------------------------------------------------
# Загружаем данные из файла students.json и находим данные о студентах с got_a = True
with open("students.json", "r", encoding="utf-8") as file:
    actual_students = json.load(file)

best_students = [student for student in actual_students if student["got_a"]]

pprint(best_students)
