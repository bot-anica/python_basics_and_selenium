# ---------- СОЗДАНИЕ И ИСПОЛЬЗОВАНИЕ ФУНКЦИИ
print("----- СОЗДАНИЕ И ИСПОЛЬЗОВАНИЕ ФУНКЦИИ -----")

# 1. Создание функции

# def - ключевое слово для создания функции
# function_name - имя функции
# arguments - аргументы функции

# def function_name(argument):
#     ...
#     return value


# 2. Обязательные и необязательные аргументы

# Пример функции с обязательным аргументом
def great(name):
    print(f"Hello, {name}!")


great("John")  # "Hello, John!"
great()  # TypeError: great() missing 1 required positional argument: 'name'


# Пример функции с необязательным аргументом
def greet(name="World"):
    print(f"Hello, {name}!")


greet("Alice")  # "Hello, Alice!"
greet()  # "Hello, World!"
