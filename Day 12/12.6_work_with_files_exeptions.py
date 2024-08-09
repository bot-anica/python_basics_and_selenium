# --------- РАБОТА С ФАЙЛАМИ: ИСКЛЮЧЕНИЯ
import csv
import json
from pprint import pprint

print("----- РАБОТА С ФАЙЛАМИ: ИСКЛЮЧЕНИЯ -----")

# Возможные исключения при работе с файлами

# FileNotFoundError - файл не существует
# PermissionError - недостаточно прав
# IsADirectoryError - это директория
# NotADirectoryError - это не директория
# FileExistsError - файл уже существует
# OSError - непредвиденная ошибка
# ValueError - некорректное значение


# Пример исключений, при работе с файлами TXT
try:
    with open("hello.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Не достаточно прав")
except Exception as ex:
    print(f"Непредвиденное исключение: {ex}")


# Пример исключений, при работе с файлами CSV
try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=';')
        data = list(reader)
        pprint(data)
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Не достаточно прав")
except csv.Error as ex:
    print(f"Ошибка с CSV-файлом: {ex}")
except Exception as ex:
    print(f"Непредвиденное исключение: {ex}")


# Пример исключений, при работе с файлами JSON
try:
    with open("students.json", "r") as file:
        data = json.load(file)
        pprint(data)
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Не достаточно прав")
except json.JSONDecodeError as ex:
    print(f"Ошибка декодирования JSON-файла: {ex}")
except Exception as ex:
    print(f"Непредвиденное исключение: {ex}")
