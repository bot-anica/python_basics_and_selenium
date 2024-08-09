# ---------- ФУНКЦИЯ FILTER
print("----- ФУНКЦИЯ FILTER -----")

# Функция filter() применяет указанную функцию к каждому элементу итерируемого
# объекта и возвращает итератор с теми элементами, для которых функция вернула True

# Синтаксис
# filter(function, iterable)
# function - функция
# iterable - итерируемый объект

# Пример 1. Фильтрация списка чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]  # list comprehension (аналог list comprehension)
print(even_numbers)


# Пример 2. Фильтрация списка слов по длине
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)

long_words = [word for word in words if len(word) > 5]  # list comprehension (аналог list comprehension)
print(long_words)

