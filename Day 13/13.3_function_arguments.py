# ---------- АРГУМЕНТЫ ФУНКЦИИ
print("----- АРГУМЕНТЫ ФУНКЦИИ -----")


def print_name(name, age, city):
    print(f"Имя: {name};\nВозраст: {age};\nГород: {city};\n")


# Позиционные аргументы
print_name("John", 25, "New York")

# Именованные аргументы
print_name(city="New York", name="Alice", age=22)

# Позиционные и именованные аргументы
print_name("John", city="New York", age=25)


# Распаковка, используя *
products_list = ["apple", "banana", "cherry"]
print(*products_list)
print(products_list[0], products_list[1], products_list[2])


# Передача произвольного количества аргументов (*)
def order_pizza(size, *toppings):
    print(f"\nВы заказали пиццу размера {size} с добавками:")
    for topping in toppings:
        print(f"- {topping}")


order_pizza(12, "сыр", "помидоры", "моцарелла")


# Передача произвольного количества именованных аргументов (**)
def make_student(**info):
    print(f"\nИнформация о студенте:")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")


make_student(name="John", age=25, major="Computer Science")

new_student = {"name": "Alice", "age": 22, "major": "Mathematics"}
make_student(**new_student)


# Порядок передачи аргументов
# 1. Позиционные
# 2. Именованные
# 3. *args
# 4. **kwargs

def get_sum(int1, int2, name="John", *args, **kwargs):
    print(int1, int2, name, args, kwargs)
    return int1 + int2


get_sum(1, 2, "Alice", "Bob", "Charlie", new_student)
