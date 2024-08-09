# ---------- EXCEPTIONS
print("----- EXCEPTIONS -----")

# Встроенные исключения
# TypeError - неверный тип данных
# ValueError - неверное значение
# FileNotFoundError - не найден файл
# ZeroDivisionError - деление на ноль


# ---------- ПРИМЕРЫ ----------
print("----- ПРИМЕРЫ -----")

# TypeError
print("TypeError")
try:
    print("hello" + 1)
except TypeError:
    print("Неверный тип данных")

# ValueError
print("\nValueError")
try:
    print(int("hello"))
except ValueError:
    print("Неверное значение")

# FileNotFoundError
print("\nFileNotFoundError")
try:
    open("hello.txt")
except FileNotFoundError:
    print("Не найден файл")

# ZeroDivisionError
print("\nZeroDivisionError")
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Деление на ноль")
