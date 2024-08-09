# ---------- ЗНАКОМСТВО С ПЕРЕМЕННЫМИ
print("----- Variables -----")

myName = "John"
currentUserName = myName
print(id(myName), myName)
print(id(currentUserName), currentUserName)

# ---------- ТИПЫ ДАННЫХ
print("\n----- DATA TYPES -----")

# Список типов данных
# int() - целое число
# float() - дробное число
# str() - строка
# bool() - логическое значение

name = "John"
age = 30
height = 2
is_student = True
is_married = False

# Виды кавычек в Python
# '' - одинарные
# "" - двойные
# ''' ''' - тройные (многострочные)
# """ """ - четверные (многострочные)

# type() - функция, которая показывает тип данных

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(is_married))

# ---------- ПРЕОБРАЗОВАНИЕ ТИПОВ ДАННЫХ
print("\n----- TYPE CONVERSION -----")

age = bool(age)
height = float(height)
is_student = str(is_student)
is_married = int(is_married)

print(type(age), age)
print(type(height), height)
print(type(is_student), is_student)
print(type(is_married), is_married)
