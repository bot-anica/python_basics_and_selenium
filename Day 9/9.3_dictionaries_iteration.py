# ---------- DICTIONARIES ITERATION
print("----- DICTIONARIES ITERATION -----")

# Итерация по словарю с одним уровнем вложенности
print("Итерация по словарю с одним уровнем вложенности")

numbers = {
    "one": 1,
    "two": 2,
    "three": 3
}

for key in numbers.keys():
    print(key)

for value in numbers.values():
    print(value)

for key, value in numbers.items():
    print(f"{key} - {value}")


# Итерация по словарю с двумя уровнями вложенности
print("\nИтерация по словарю с двумя уровнями вложенности")

nested_numbers = {
    "one": {"a": 1, "b": 2},
    "two": {"c": 3, "d": 4},
    "three": {"e": 5, "f": 6}
}

for key in nested_numbers.keys():
    for nested_key in nested_numbers[key].keys():
        print(f"{key} - {nested_key} - {nested_numbers[key][nested_key]}")

for value in nested_numbers.values():
    for nested_value in value.values():
        print(nested_value)

for key, value in nested_numbers.items():
    for nested_key, nested_value in value.items():
        print(f"{key} - {nested_key} - {nested_value}")