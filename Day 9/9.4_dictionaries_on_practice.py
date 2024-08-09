from pprint import pprint

from marvel import full_dict as marvel_full_dict

# ---------- DICTIONARIES ON PRACTICE
print("----- DICTIONARIES ON PRACTICE -----")


def save_search_result(film_id, r_list, r_dict, film):
    r_list.append(film)
    r_dict[film_id] = film


def search_films(search_key, search_query, films):
    result_list = []
    result_dict = {}

    for key, film in films.items():
        if search_key == "year":
            if search_query == film[search_key]:
                save_search_result(key, result_list, result_dict, film)
        else:
            if search_query.lower() in film[search_key].lower():
                save_search_result(key, result_list, result_dict, film)

    return {"result_list": result_list, "result_dict": result_dict}


available_search_key_questions = {
    "title": "Найти фильм по названию",
    "year": "Найти фильм по году",
}


def ask_search_key():
    key_index = input(
        "По какому полю искать?\n"
        "\t1 - title\n"
        "\t2 - year\n"
    )

    if key_index.isnumeric() and int(key_index) in range(1, 6):
        return int(key_index) - 1
    else:
        print("Неверный ввод")
        return ask_search_key()


def ask_search_query():
    query = input(available_search_key_questions[search_key] + "\n")

    if query.isnumeric():
        return int(query)
    else:
        return query


search_key_index = ask_search_key()
search_key = list(available_search_key_questions.keys())[search_key_index]
search_query = ask_search_query()

search_result = search_films(search_key, search_query, marvel_full_dict)

pprint(search_result["result_list"])
# pprint(search_result["result_dict"])
