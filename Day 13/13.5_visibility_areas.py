# ---------- ОБЛАСТИ ВИДИМОСТИ
print("----- ОБЛАСТИ ВИДИМОСТИ -----")

# Область видимости - это пространство, в котором определены переменные и функции


# Пример области видимости

global_variable = "I am global variable!"


def my_function():
    local_variable = "I am local variable!"
    print(global_variable)
    print(local_variable)


my_function()

print(global_variable)

# print(local_variable)  # NameError: name 'local_variable' is not defined


# nonlocal - позволяет изменять переменную внешней области видимости
print("\nnonlocal - позволяет изменять переменную внешней области видимости")

# Пример без использования nonlocal
print("\nПример без использования nonlocal")


def outer_1():
    outer_variable = "I am OUTER variable!"

    def inner():
        outer_variable = "I am INNER variable!"
        print(outer_variable)  # "I am INNER variable!"

    inner()
    print(outer_variable)  # "I am OUTER variable!"


outer_1()

# Пример с использованием nonlocal
print("\nПример с использованием nonlocal")


def outer_2():
    outer_variable = "I am OUTER!"

    def inner():
        nonlocal outer_variable
        outer_variable = "I am INNER variable!"
        print(outer_variable)  # "I am INNER variable!"

    inner()
    print(outer_variable)  # "I am INNER variable!"


outer_2()
