# ---------- ФУНКЦИЯ SORTED
print("----- ФУНКЦИЯ SORTED -----")


# Функция sorted() сортирует итерируемый объект и возвращает отсортированный список

# Синтаксис
# sorted(iterable, key=None, reverse=False)
# iterable - итерируемый объект
# key - функция сортировки
# reverse - параметр, указывающий на то, следует ли сортировка в обратном порядке


# Сортировка List
numbers = [5, 3, 8, 1, 9, 2, 7, 6, 4]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# Сортировка Dict по ключу
marks = {"Math": 5, "Geography": 3, "English": 4, "Biology": 5, "History": 3}
sorted_marks = sorted(marks.items(), key=lambda x: x[0]) # сортировка по ключу (по имени)
print(sorted_marks)


# Сортировка Dict по значению
sorted_marks = sorted(marks.items(), key=lambda x: x[1], reverse=True) # сортировка по значению (по оценке)
print(sorted_marks)


# Сортировка List[Dict] по значениям ключа "age"
users = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Jack", "age": 20},
]
sorted_users = sorted(users, key=lambda x: x["age"])
print(sorted_users)
