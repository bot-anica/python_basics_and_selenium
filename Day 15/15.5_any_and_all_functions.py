# ---------- ФУНКЦИИ ANY И ALL
print("----- ФУНКЦИИ ANY И ALL -----")


# Функция any() возвращает True, если хотя бы один элемент истинный
# Функция all() возвращает True, если все элементы истинные


# Пример 1. Простые примеры использования функций any() и all()
numbers = [1, 2, 3, 4, 5]
print(any(numbers))  # True
print(all(numbers))  # True

numbers = [0, 2, 3, 4, 5]
print(any(numbers))  # True
print(all(numbers))  # False


# Пример 2. Проверка на наличие цифры в строке
some_string = "hello4564"
print(any(char.isdigit() for char in some_string))  # True
print(all(char.isdigit() for char in some_string))  # False


# Пример 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Проверка на наличие числа 2 в матрице
print(any(2 in row for row in matrix))  # True

# Проверка на то, что все элементы в матрице являются 2
print(all(2 in row for row in matrix))  # False

# Проверка на то, что все элементы в матрице являются цифрами
# Перебираем все строки: all(row for row in matrix)
# Перебираем все элементы в строке: all(num for num in row)
# Проверяем являются ли элемент числом: isinstance(num, int)

# isinstance(num, int)
# all(isinstance(num, int) for num in row)
# all(all(isinstance(num, int) for num in row) for row in matrix)

print(all(all(isinstance(num, int) for num in row) for row in matrix))  # True
