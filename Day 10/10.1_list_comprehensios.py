# ---------- LIST COMPREHENSIONS
print("----- LIST COMPREHENSIONS -----")


# ---------- Простая копия списка ----------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = []

# Обычный вариант
for x in numbers:
    numbers_2.append(x)

# Продвинутый вариант
numbers_3 = [x for x in numbers]

print("\nПростая копия списка")
print(f"Результат 1: {numbers_2}")
print(f"Результат 2: {numbers_3}")


# ---------- Копия списка с условием ----------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = []

# Обычный вариант
for x in numbers:
    if x % 2 == 0:
        numbers_2.append(x)

# Продвинутый вариант
numbers_3 = [x for x in numbers if x % 2 == 0]

print("\nКопия списка с условием")
print(f"Результат 1: {numbers_2}")
print(f"Результат 2: {numbers_3}")


# ---------- Копия двух списков в один со всеми возможными комбинациями ----------
names_1 = ["Alex", "Beth", "Caroline"]
names_2 = ["Gina", "Holly", "Ida"]

concatenated_names = []

# Обычный вариант
for name_1 in names_1:
    for name_2 in names_2:
        concatenated_names.append(name_1 + " " + name_2 + "!")

# Продвинутый вариант
concatenated_names_2 = [name_1 + " " + name_2 + "!" for name_1 in names_1 for name_2 in names_2]

print("\nКопия двух списков в один со всеми возможными комбинациями")
print(f"Результат 1: {concatenated_names}")
print(f"Результат 2: {concatenated_names_2}")

