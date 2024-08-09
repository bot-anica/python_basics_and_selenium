# ---------- LISTS
print("----- LISTS -----")

# Списки (list)
# Список представляет собоей упорядоченный набор элементов (ORDERED, CHANGEABLE, ALLOWED DUPLICATES)

first_list = [1, 2, 3, 4, 5]
second_list = list("Hello, World!")
third_list = [i for i in range(10)]

# Пустые списки
empty_list = []
empty_list_2 = list()

# Проверка вхождения элемента в список
shop_list = ["milk", "bread", "butter", "cheese", "eggs"]
if "cheese" in shop_list:
    print("Cheese is in shop_list")
else:
    print("Cheese is not in shop_list")

# Итерация по списку
for item in shop_list:
    print(item)
