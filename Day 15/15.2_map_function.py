# ---------- ФУНКЦИЯ MAP
print("----- ФУНКЦИЯ MAP -----")

# Функция map() применяет указанную функцию к каждому элементу итерируемого
# объекта и возвращает итератор с новыми значениями

# Синтаксис
# map(function, iterable)
# function - функция
# iterable - итерируемый объект

# Пример 1. Преобразование списка чисел в список их квадратов
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# Пример 2. Приведение всех символов в строке к верхней регистру
names = ["John", "Jane", "Jack"]
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)

# Пример 3. Использование map() с несколькими последовательностями
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

result = list(map(lambda x, y: x * y, numbers_1, numbers_2))
print(result)


# Пример 4. Использование if внутри lambda функции map()
def get_int(x):
    if x.isdigit():
        return int(x)
    else:
        return 0


numbers_input = input("Enter a list of numbers separated by spaces: ").split()

# Преобразование введенного пользователем списка в список чисел с использованием map() и lambda
result = list(map(lambda x: int(x) if x.isdigit() else 0, numbers_input))
print(result)

# Преобразование введенного пользователем списка в список чисел с использованием map() и обычной функции
result = list(map(get_int, numbers_input))
print(result)

# Преобразование введенного пользователем списка в список чисел с list comprehension
result = [int(x) if x.isdigit() else 0 for x in numbers_input]
print(result)

result = [get_int(x) for x in numbers_input]
print(result)
