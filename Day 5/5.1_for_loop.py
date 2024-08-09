# ---------- FOR LOOP
print("----- FOR LOOP -----")

# Итеррируемые объекты
# Строка (string): строка представляет соьой последовательность символов
# Список (list): список представляет собоей упорядоченный набор элементов (ORDERED, CHANGEABLE, ALLOWED DUPLICATES)
# Кортеж (tuple): кортеж представляет собоей упорядоченный набор элементов (ORDERED, UNCHANGEABLE, ALLOWED DUPLICATES)
# Словарь (dict): словарь представляет собоей набор пар "ключ-значение" (ORDERED, CHANGEABLE, DUPLICATES NOT ALLOWED)
# Множество (set): множество представляет собоей набор неповторяющихся элементов (UNORDERED, UNCHANGEABLE, DUPLICATES NOT ALLOWED)

film_name = "Interstellar"

char_e_counter = 0

for char in film_name:
    if char == "e":
        char_e_counter += 1

print(f"Film name: {film_name}\nChar 'e' count: {char_e_counter}")