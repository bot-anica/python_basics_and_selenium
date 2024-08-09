# Типизация функций
from typing import List, Callable

interests: List[str] = ["music", "reading", "travelling", "cooking"]

# 1. Указываем тип аргументов функции, в данном случае "interests_list: List[str]"
# 2. Указываем тип возвращаемого значения функции, в данном случае "List[str]"
def get_sorted_interests_list(interests_list: List[str]) -> List[str]:
    return sorted(interests_list)


print(get_sorted_interests_list(interests))


# Типизация lambda функций

# Для типизации lambda функций используется Callable из библиотеки typing
# Callable принимает два аргумента: первый - тип аргументов, второй - тип возвращаемого значения
get_reverse_sorted_interests_list: Callable[[List[str]], List[str]] = lambda interests_list: (
    sorted(interests_list, reverse=True)
)

print(get_reverse_sorted_interests_list(interests))
