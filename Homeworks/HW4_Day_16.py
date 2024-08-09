from typing import Optional, Set

from cities import cities

# Переписать игру Города используя функции

# Требования к программе:
# 1. Использование функций
# 2. Соблюдение принципов DRY и SRP
# 3. Аннотация типов
# 4. Документация для каждой функции


cities_set = {city["name"] for city in cities}

user_is_win = False
robot_is_win = False
last_city_name = ""
next_first_letter = ""


def get_next_first_letter() -> str:
    """
    :return: Последняя допустимая буква в названии города (первая буква следующего города)
    """

    letter_index = len(last_city_name) - 1
    bad_letters = ["й", "ь", "ъ", "ё", "ы"]

    while letter_index >= 0:
        if last_city_name[letter_index].isalpha() and (last_city_name[letter_index] not in bad_letters):
            return last_city_name[letter_index]

        letter_index -= 1


def get_cities_starting_by_target_letter() -> Set[str]:
    """
    :return: Название города, начинающееся на букву, которая указана в next_first_letter
    """

    return {name for name in cities_set if name.lower().startswith(next_first_letter)}


def check_existing_cities_on_starting_letter() -> bool:
    """
    :return: Есть ли в наборе городов города, начинающиеся на букву, которая указана в next_first_letter
    """

    cities_starting_by_target_letter = get_cities_starting_by_target_letter()
    return len(cities_starting_by_target_letter) > 0


def check_if_cities_list_is_empty() -> bool:
    """
    :return: Есть ли в списке городов города
    """

    return len(cities_set) == 0


def user_step() -> Optional[str]:
    """
    :return: Название города
    """

    global user_is_win
    global robot_is_win
    global last_city_name
    global next_first_letter

    user_input = get_user_city()

    if check_if_user_wrote_stop(user_input):
        robot_is_win = True

    if check_if_user_wrote_unknown_city(user_input):
        robot_is_win = True

    if user_input in cities_set:
        cities_set.remove(user_input)
        last_city_name = user_input
        next_first_letter = get_next_first_letter()

        print(f"Вы ввели: {user_input}")

        if not check_existing_cities_on_starting_letter():
            user_is_win = True

        return user_input
    else:
        robot_is_win = True


def robot_step() -> None:
    global last_city_name
    global next_first_letter
    global robot_is_win

    print(f"Следующий город должен начинаться на букву \"{next_first_letter}\"")

    cities_starting_by_target_letter = get_cities_starting_by_target_letter()

    robot_city_name = cities_starting_by_target_letter.pop()

    if check_if_cities_list_is_empty():
        robot_is_win = True

    print(f"Противник назвал город: {robot_city_name}")

    cities_set.remove(robot_city_name)
    last_city_name = robot_city_name
    next_first_letter = get_next_first_letter()


def get_user_city() -> str:
    """
    :return: Название города, введенное пользователем
    """

    if last_city_name:
        return input(f'\nВведите название города!\nОно должно начинаться на букву "{next_first_letter}"\n')
    else:
        return input("\nВведите название города!\n")


def check_if_user_wrote_city(value: str) -> bool:
    """
    :param value: название города
    :return: bool, если пользователь ввел название города
    """

    return value != ""


def check_if_robot_wrote_city(value: str) -> bool:
    """
    :param value: название города
    :return: bool, если робот ввел название города
    """

    return value == ""


def check_if_user_wrote_stop(value: str) -> bool:
    """
    :param value: название города
    :return: bool, если пользователь ввел слово "стоп"
    """

    return value == "стоп"


def check_if_user_wrote_unknown_city(value: str) -> bool:
    """
    :param value: название города
    :return: bool, если пользователь ввел несуществующее название города
    """

    return next_first_letter and value and value[0].lower() != next_first_letter


def show_result():
    if user_is_win:
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")


def start_game():
    global last_city_name
    global next_first_letter
    global user_is_win
    global robot_is_win

    while not (user_is_win or robot_is_win):
        print(f"Осталось городов: {len(cities_set)}")

        user_city = user_step()

        if not check_if_user_wrote_city(user_city):
            continue

        if not user_is_win and not robot_is_win:
            robot_step()

    show_result()


start_game()
