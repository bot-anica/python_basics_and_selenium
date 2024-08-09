# ---------- SET COMPREHENSIONS
print("----- SET COMPREHENSIONS -----")

# ---------- Простая копия сета ----------
guests = {
    "John Smith",
    "Jane Smith",
    "Alex Johnson",
    "Jessica Johnson",
    "Alice Brown",
    "Bob Brown"
}

# Обычный вариант
result = set()

for guest in guests:
    result.add(guest)

# Продвинутый вариант
result_2 = {guest for guest in guests}

print("\nПростая копия сета")
print(f"Результат 1: {result}")
print(f"Результат 2: {result_2}")


# ---------- Копия сета с условием ----------
guests = {
    "John Smith",
    "Jane Smith",
    "Alex Johnson",
    "Jessica Johnson",
    "Alice Brown",
    "Bob Brown",
    "Sandy Brown",
    "Anna Bernard",
    "Kenny White"
}

# Обычный вариант
result = set()

for guest in guests:
    if "j" in guest.lower():
        result.add(guest)

# Продвинутый вариант
result_2 = {guest for guest in guests if "j" in guest.lower()}
result_3 = {guest for guest in guests if [name.split()[1] for name in guests].count(guest.split()[1]) > 1}

print("\nКопия сета с условием")
print(f"Результат 1: {result}")
print(f"Результат 2: {result_2}")
print(f"Результат 3: {result_3}")


# ---------- Копия двух сетов в один со всеми возможными комбинациями ----------
names_1 = {"Alex", "Beth", "Caroline"}
names_2 = {"Gina", "Holly", "Ida"}

# Обычный вариант
result = set()

for name_1 in names_1:
    for name_2 in names_2:
        result.add(name_1 + " " + name_2 + "!")

# Продвинутый вариант
result_2 = {name_1 + " " + name_2 + "!" for name_1 in names_1 for name_2 in names_2}

print("\nКопия двух сетов в один со всеми возможными комбинациями")
print(f"Результат 1: {result}")
print(f"Результат 2: {result_2}")