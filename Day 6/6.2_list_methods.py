# ---------- LIST METHODS
print("----- LIST METHODS -----")

# append() - добавляет элемент в конец списка
# extend() - добавляет элементы в конец списка
# insert() - добавляет элемент в список по указанной позиции
# remove() - удаляет первый вхождение указанного элемента
# pop() - удаляет элемент по указанной позиции
# clear() - очищает список
# index() - возвращает индекс первого вхождения указанной подстроки
# count() - подсчитывает количество вхождений подстроки
# sort() - сортирует список
# sort(reverse=True) - сортирует список в обратном порядке
# reverse() - разворачивает список
# copy() - создает копию списка
# len() - возвращает длину списка
# del() - удаляет элемент по указанной позиции, диапазон элементов или весь список
# (del list[index], del list[start:stop], del list[start:stop:step], del list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
numbers.append(11)
print(numbers)
numbers.extend([12, 13, 14, 15])
print(numbers)
numbers.insert(0, -1)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(3)
print(numbers)
print(numbers.index(4))
print(numbers.count(4))
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.copy())
print(len(numbers))

del numbers[0:5]
print(numbers)

numbers.clear()
print(numbers)
