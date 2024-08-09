from marvel import full_dict as marvel_full_dict, small_dict as marvel_small_dict

# ---------- DICTIONARY COMPREHENSIONS
print("----- DICTIONARY COMPREHENSIONS -----")

# ---------- Простая копия словаря ----------
party_guests = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 1,
    "David": 3,
    "Eve": 1,
    "Fred": 1,
}

# Обычный вариант
copied_party_guests = {}

for guest, number in party_guests.items():
    copied_party_guests[guest] = number

# Продвинутый вариант
copied_party_guests_2 = {guest: number for guest, number in party_guests.items()}

print("\nПростая копия словаря")
print(f"Результат 1: {copied_party_guests}")
print(f"Результат 2: {copied_party_guests_2}")


# ---------- Копия словаря с условием ----------
party_guests = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 1,
    "David": 3,
    "Eve": 1,
    "Fred": 1,
}

# Обычный вариант
copied_party_guests = {}

for guest, number in party_guests.items():
    if number > 1:
        copied_party_guests[guest] = number

# Продвинутый вариант
copied_party_guests_2 = {guest: number for guest, number in party_guests.items() if number > 1}

print("\nПростая копия словаря")
print(f"Результат 1: {copied_party_guests}")
print(f"Результат 2: {copied_party_guests_2}")

films_without_year = {film: year for film, year in marvel_small_dict.items() if year is None}
films_in_first_stage = {film["title"]: film["year"] for film in marvel_full_dict.values() if film["stage"] == "Первая фаза"}

print(f"Фильмы без года: {films_without_year}")
print(f"Фильмы в первой фазе: {films_in_first_stage}")

