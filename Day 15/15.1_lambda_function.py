from functools import reduce

# ---------- ЛЯМБДА ФУНКЦИЯ
print("----- ЛЯМБДА ФУНКЦИЯ -----")

# Лямбда функция - это функция, которая принимает какие-то аргументы,
# но не имеет имени (называется "анонимной" функцией)

# Синтаксис лямбда функции
# lambda arguments: expression


# Ограничения при использовании лямбда функции
# 1. Не может содержать несколько выражений
# 2. Не может содержать команды return
# 3. Не может содержать команды raise, break, continue, yield
# 4. Не может содержать несколько ветвлений (if, elif, else)


# Пример лямбда функции

# Использование лямбда функции с функцией map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# Использование лямбда функции с функцией filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Использование лямбда функции с функцией reduce()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Использование лямбда функции с функцией sorted()
marks = {"Math": 5, "Geography": 3, "English": 4, "Biology": 5, "History": 3}
sorted_marks = sorted(marks.items(), key=lambda x: x[1])
print(sorted_marks)
