from cities import cities

cities_set = {city["name"] for city in cities}

user_is_win = False
robot_is_win = False
last_city_name = ""
next_first_letter = ""


def get_next_first_letter(city_name):
    letter_index = len(city_name) - 1
    bad_letters = ["й", "ь", "ъ", "ё", "ы"]

    while letter_index >= 0:
        if city_name[letter_index].isalpha() and city_name[letter_index] not in bad_letters:
            return city_name[letter_index]

        letter_index -= 1


def robot_step(last_city_name):
    first_letter = get_next_first_letter(last_city_name)

    print(f"Текущее название города: {last_city_name}.\n"
          f"Следующий город должен начинаться на букву \"{first_letter}\"")

    next_city_name = {name for name in cities_set if name.lower().startswith(first_letter)}

    if len(next_city_name) == 0:
        return None
    else:
        next_city_name = next_city_name.pop()

    if next_city_name:
        cities_set.remove(next_city_name)
        print(f"Следующее название города: {next_city_name}")
        return next_city_name


def start_game():
    global last_city_name
    global next_first_letter
    global user_is_win
    global robot_is_win

    while not (you_are_win or robot_is_win):
        if last_city_name:
            user_input = input(f'\nВведите название города!\nОно должно начинаться на букву "{next_first_letter}"\n')
        else:
            user_input = input("\nВведите название города!\n")

        if user_input == "стоп" or user_input == "":
            robot_is_win = True

        if len(user_input) > 0 and next_first_letter and user_input[0].lower() != next_first_letter:
            robot_is_win = True

        if user_input in cities_set:
            cities_set.remove(user_input)
            last_city_name = user_input
            print(f"Вы ввели: {user_input}")
            robot_city_name = robot_step(last_city_name)

            if robot_city_name:
                last_city_name = robot_city_name
                next_first_letter = get_next_first_letter(robot_city_name)
            else:
                you_are_win = True

            if not cities_set:
                you_are_win = True
        else:
            robot_is_win = True

        print(f"Осталось городов: {len(cities_set)}")

    if you_are_win:
        print("Вы выиграли!")
    elif robot_is_win:
        print("Вы проиграли!")


start_game()
