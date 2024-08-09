# ---------- RANGE AND ENUMERATE
print("----- RANGE AND ENUMERATE -----")

# range() - генератор последовательности чисел
# enumerate() - принимает последовательность и возвращает итератор с индексами

products_list = ["milk", "bread", "butter", "cheese", "eggs"]

# Variant 1 - range
print("\n# Variant 1 - range")
for i in range(len(products_list)):
    print(products_list[i])

# Variant 2 - enumerate
print("\n# Variant 2 - enumerate")
for index, product in enumerate(products_list):
    print(f"{index + 1}. {product}")  # INDEX + 1 because enumerate starts from 0

# Variant 3 - enumerate with start
print("\n# Variant 3 - enumerate with start")
for index, product in enumerate(products_list, start=1):
    print(f"{index}. {product}")  # just INDEX because we use start=1 in enumerate function to start from 1 instead of 0

user_choice = int(input("Enter number of product: "))

if user_choice > len(products_list):
    user_choice = len(products_list)

if user_choice < 1:
    user_choice = 1

print(products_list[user_choice - 1])
