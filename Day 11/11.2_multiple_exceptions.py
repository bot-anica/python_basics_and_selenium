# ---------- MULTIPLE EXCEPTIONS
print("----- MULTIPLE EXCEPTIONS -----")

# ---------- ПРИМЕРЫ ----------
print("----- ПРИМЕРЫ -----")

try:
    open("hello.txt")
    pass
except FileNotFoundError as fne:  # fne - пользовательская переменная для доступа к ошибке
    print(f"File {fne.filename} not found.")  # fne.filename - имя файла, при попытке открыть несуществующий файл
    pass
except ZeroDivisionError as zde:  # zde - пользовательская переменная для доступа к ошибке
    print(f"Cannot divide by zero: {zde}")
    pass
