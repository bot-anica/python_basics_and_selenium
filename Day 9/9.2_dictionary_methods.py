# ---------- DICTIONARY METHODS
print("----- DICTIONARY METHODS -----")

# copy() - создает копию словаря
# fromkeys() - создает словарь с указанными ключами
# get(key, default) - возвращает значение по указанной позиции или значение по умолчанию
# keys() - возвращает список ключей словаря
# values() - возвращает список значений словаря
# items() - возвращает пары "ключ - значение" словаря
# pop() - удаляет элемент по указанной позиции
# popitem() - удаляет и возвращает пару "ключ - значение"
# setdefault(key, default) - возвращает значение по указанной позиции или вставляет значение по умолчанию
# update(dict) - обновляет словарь, добавляя пары "ключ - значение" из указанного словаря
# clear() - очищает словарь

# copy() - создает копию словаря
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
shopping_list_copy = shopping_list.copy()
print('copy() - создает копию словаря: \n{"milk": 1, "bread": 2, "butter": 3}.copy()')
print(f"Результат: {shopping_list_copy}\n")

# fromkeys() - создает словарь с указанными ключами
# shopping_list = {}
# shopping_list = dict.fromkeys(["milk", "bread", "butter"], 1)
# print('fromkeys() - создает словарь с указанными ключами: {"milk": 1, "bread": 1, "butter": 1}.fromkeys(["milk", "bread", "butter"], 1)')
# print(f"Результат: {shopping_list}")

# get(key, default) - возвращает значение по указанной позиции или значение по умолчанию
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('get(key, default) - возвращает значение по указанной позиции или значение по умолчанию: \n'
      '{"milk": 1, "bread": 2, "butter": 3}.get("milk")')
print(f"Результат: {shopping_list.get('milk')}\n")

# keys() - возвращает список ключей словаря
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('keys() - возвращает список ключей словаря: \n{"milk": 1, "bread": 2, "butter": 3}.keys()')
print(f"Результат: {shopping_list.keys()}\n")

# values() - возвращает список значений словаря
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('values() - возвращает список значений словаря: \n{"milk": 1, "bread": 2, "butter": 3}.values()')
print(f"Результат: {shopping_list.values()}\n")

# items() - возвращает пары "ключ - значение" словаря
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('items() - возвращает пары "ключ - значение" словаря: \n{"milk": 1, "bread": 2, "butter": 3}.items()')
print(f"Результат: {shopping_list.items()}\n")

# pop() - удаляет элемент по указанной позиции
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('pop() - удаляет элемент по указанной позиции: \n{"milk": 1, "bread": 2, "butter": 3}.pop("milk")')
print(f"Результат: {shopping_list.pop('milk')}\n")

# popitem() - удаляет и возвращает пару "ключ - значение"
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('popitem() - удаляет и возвращает пару "ключ - значение": \n{"milk": 1, "bread": 2, "butter": 3}.popitem()')
print(f"Результат: {shopping_list.popitem()}\n")

# setdefault(key, default) - возвращает значение по указанной позиции или устанавливает значение по умолчанию
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
print('setdefault(key, default) - возвращает значение по указанной позиции или устанавливает значение по умолчанию: \n'
      '{"milk": 1, "bread": 2, "butter": 3}.setdefault("eggs", 0)')
print(f"Результат: {shopping_list.setdefault('eggs', 0)}\n")

# update() - обновляет словарь
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
shopping_list.update({'eggs': 0, 'cheese': 4})
print('update() - обновляет словарь: \n{"milk": 1, "bread": 2, "butter": 3}.update({"eggs": 0, "cheese": 4})')
print(f"Результат: {shopping_list}\n")

# clear() - очищает словарь
shopping_list = {"milk": 1, "bread": 2, "butter": 3}
shopping_list.clear()
print('clear() - очищает словарь: \n{"milk": 1, "bread": 2, "butter": 3}.clear()')
print(f"Результат: {shopping_list}\n")
