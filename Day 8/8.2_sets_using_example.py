# -------- МНОЖЕСТВА - ПРИМЕР ПРИМЕНЕНИЯ
print("----- МНОЖЕСТВА - ПРИМЕР ПРИМЕНЕНИЯ -----")

pokemons_alice = {
    "Caterpie",
    "Metapod",
    "Charmander",
    "Squirtle",
    "Bulbasaur",
    "Snorlax",
    "Pikachu",
    "Jigglypuff"
}

pokemons_bob = {
    "Caterpie",
    "Metapod",
    "Bulbasaur",
    "Pidgey",
    "Pikachu",
    "Jigglypuff",
    "Pidgeotto",
    "Pidgeot"
}

# ПОИСК ПЕРЕСЕЧЕНИЯ ПОКЕМОНОВ Алисы и Боба
# intersection() - возвращает пересечение множеств (мат. оператор: &)

common_pokemons = pokemons_bob.intersection(pokemons_alice)
common_pokemons_2 = pokemons_bob & pokemons_alice

print("Пересечение множеств pokemons_alice и pokemons_bob: ")
print(common_pokemons)
print(common_pokemons_2)


# ПОИСК УНИКАЛЬНЫХ ПОКЕМОНОВ Боба
# difference() - возвращает разность множеств (мат. оператор: -)

bob_unique_pokemons = pokemons_bob.difference(pokemons_alice)
bob_unique_pokemons_2 = pokemons_bob - pokemons_alice

print("Уникальные покемоны Боба: ")
print(bob_unique_pokemons)
print(bob_unique_pokemons_2)


# КОМАНДА ВСЕХ УНИКАЛЬНЫХ ПОКЕМОНОВ Алисы и Боба
# union() - возвращает объединение множеств (мат. оператор: |)

all_unique_pokemons = pokemons_alice.union(pokemons_bob)
all_unique_pokemons_2 = pokemons_alice | pokemons_bob

print("Команда всех уникальных покемонов Алисы и Боба: ")
print(all_unique_pokemons)
print(all_unique_pokemons_2)


# Поиск всех покемонов, кроме тех, которые есть у обоих
# symmetric_difference() - возвращает симметрическую разность множеств (мат. оператор: ^)

all_pokemons_without_common = pokemons_alice.symmetric_difference(pokemons_bob)
all_pokemons_without_common_2 = pokemons_alice ^ pokemons_bob

print("Команда всех покемонов, кроме тех, которые есть у обоих: ")
print(all_pokemons_without_common)
print(all_pokemons_without_common_2)
