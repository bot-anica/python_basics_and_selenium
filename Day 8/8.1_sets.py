# ---------- SETS
import timeit

print("----- SETS -----")

# Множества (set)
# Множество представляет собоей набор уникальных элементов (UNIQUE, UNCHANGEABLE, NO DUPLICATES)
# Множество неизменяемо, но мы можем добавлять и удалять элементы
# Множества могут содержать числа, строки и картежи

right_set = {1, "hello", (1, 2, 3)}
# wrong_set = {1, "hello", [1, 2, 3]}  # TypeError: unhashable type: 'list'

# Методы множества
# in - проверяет наличие элемента в множестве
# add() - добавляет элемент в множество
# update() - добавляет элементы в множество
# copy() - создает копию множества
# len() - возвращает длину множества
# set() - создает множество из списка
# difference() - возвращает разницу множеств
# difference_update() - удаляет все элементы, присутствующие в другом множестве
# intersection() - возвращает пересечение множеств
# intersection_update() - оставляет в множестве только элементы, присутствующие в другом множестве
# symmetric_difference() - возвращает симметричную разницу множеств
# symmetric_difference_update() - возвращает симметричную разницу множеств и обновляет первое множество
# union() - возвращает объединение множеств
# update() - возвращает объединение множеств и обновляет первое множество
# issubset() - возвращает True, если первое множество является подмножеством второго множества
# issuperset() - возвращает True, если первое множество является супермножеством второго множества
# isdisjoint() - возвращает True, если множества не имеют общих элементов
# discard() - удаляет элемент из множества
# remove() - удаляет элемент из множества
# pop() - удаляет случайный элемент из множества
# clear() - очищает множество

# in - проверяет наличие элемента в множестве
numbers = {1, 2, 3, 4, 5}
print(f"1 in {1, 2, 3, 4, 5}")
print(f"Результат: {1 in numbers}\n")

# add() - добавляет элемент в множество
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(f"add() - добавляет элемент в множество:\n{1, 2, 3, 4, 5}.add(6)")
print(f"Результат: {numbers}\n")

# update() - добавляет элементы в множество
numbers = {1, 2, 3, 4, 5}
numbers.update([7, 8, 9, 10])
print(f"update() - добавляет элементы в множество:\n{1, 2, 3, 4, 5}.update([7, 8, 9, 10])")
print(f"Результат: {numbers}\n")

# copy() - создает копию множества
numbers = {1, 2, 3, 4, 5}
numbers_copy = numbers.copy()
print(f"copy() - создает копию множества:\n{1, 2, 3, 4, 5}.copy()")
print(f"Результат: {numbers_copy}\n")

# len() - возвращает длину множества
numbers = {1, 2, 3, 4, 5}
print(f"len() - возвращает длину множества:\n{1, 2, 3, 4, 5}.len()")
print(f"Результат: {len(numbers)}\n")

# set() - создает множество из списка
numbers = [1, 2, 3, 4, 5]
numbers_set = set(numbers)
print(f"set() - создает множество из списка:\n[1, 2, 3, 4, 5].set()")
print(f"Результат: {numbers_set}\n")

# difference() - возвращает разницу множеств
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers_difference = numbers.difference(numbers_2)
print(f"difference() - возвращает разницу множеств:\n{1, 2, 3, 4, 5}.difference({4, 5, 6, 7, 8})")
print(f"Результат: {numbers_difference}\n")

# difference_update() - удаляет все элементы, присутствующие в другом множестве
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers.difference_update(numbers_2)
print(f"difference_update() - удаляет все элементы, присутствующие в другом множестве:\n"
      f"{1, 2, 3, 4, 5}.difference_update({4, 5, 6, 7, 8})")
print(f"Результат: {numbers}\n")

# intersection() - возвращает пересечение множеств
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers_intersection = numbers.intersection(numbers_2)
print(f"intersection() - возвращает пересечение множеств:\n{1, 2, 3, 4, 5}.intersection({4, 5, 6, 7, 8})")
print(f"Результат: {numbers_intersection}\n")

# intersection_update() - удаляет все элементы, не присутствующие в другом множестве
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers.intersection_update(numbers_2)
print(f"intersection_update() - удаляет все элементы, не присутствующие в другом множестве:\n"
      f"{1, 2, 3, 4, 5}.intersection_update({4, 5, 6, 7, 8})")
print(f"Результат: {numbers}\n")

# symmetric_difference() - возвращает симметрическую разницу множеств
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers_symmetric_difference = numbers.symmetric_difference(numbers_2)
print(f"symmetric_difference() - возвращает симметрическую разницу множеств:\n"
      f"{1, 2, 3, 4, 5}.symmetric_difference({4, 5, 6, 7, 8})")
print(f"Результат: {numbers_symmetric_difference}\n")

# symmetric_difference_update() - удаляет все элементы, присутствующие в другом множестве
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers.symmetric_difference_update(numbers_2)
print(f"symmetric_difference_update() - удаляет все элементы, присутствующие в другом множестве:\n"
      f"{1, 2, 3, 4, 5}.symmetric_difference_update({4, 5, 6, 7, 8})")
print(f"Результат: {numbers}\n")

# union() - возвращает объединение множеств
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers_union = numbers.union(numbers_2)
print(f"union() - возвращает объединение множеств:\n{1, 2, 3, 4, 5}.union({4, 5, 6, 7, 8})")
print(f"Результат: {numbers_union}\n")

# update() - добавляет элементы в множество
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
numbers.update(numbers_2)
print(f"update() - добавляет элементы в множество:\n{1, 2, 3, 4, 5}.update({4, 5, 6, 7, 8})")
print(f"Результат: {numbers}\n")

# issubset() - проверяет, является ли первое множество подмножеством второго
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
print(f"issubset() - проверяет, является ли первое множество подмножеством второго:\n"
      f"{1, 2, 3, 4, 5}.issubset({4, 5, 6, 7, 8})")
print(f"Результат: {numbers.issubset(numbers_2)}\n")

# issuperset() - проверяет, является ли первое множество супермножеством второго
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
print(f"issuperset() - проверяет, является ли первое множество супермножеством второго:\n"
      f"{1, 2, 3, 4, 5}.issuperset({4, 5, 6, 7, 8})")
print(f"Результат: {numbers_2.issuperset(numbers)}\n")

# isdisjoint() - проверяет, являются ли два множества пересекающимися
numbers = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}
print(f"isdissjoint() - проверяет, являются ли два множества пересекающимися:\n"
      f"{1, 2, 3, 4, 5}.isdissjoint({4, 5, 6, 7, 8})")
print(f"Результат: {numbers.isdisjoint(numbers_2)}\n")

# discard() - удаляет элемент из множества
numbers = {1, 2, 3, 4, 5}
numbers.discard(5)
print(f"discard() - удаляет элемент из множества:\n{1, 2, 3, 4, 5}.discard(5)")
print(f"Результат: {numbers}\n")

# remove() - удаляет элемент из множества
numbers = {1, 2, 3, 4, 5}
numbers.remove(5)
print(f"remove() - удаляет элемент из множества:\n{1, 2, 3, 4, 5}.remove(5)")
print(f"Результат: {numbers}\n")

# pop() - удаляет и возвращает случайнный элемент из множества
numbers = {1, 2, 3, 4, 5}
print(f"pop() - удаляет и возвращает случайнный элемент из множества:\n{1, 2, 3, 4, 5}.pop()")
print(f"Результат: {numbers.pop()}\n")

# clear() - очищает множество
numbers = {1, 2, 3, 4, 5}
numbers.clear()
print(f"clear() - очищает множество:\n{1, 2, 3, 4, 5}.clear()")
print(f"Результат: {numbers}\n")
