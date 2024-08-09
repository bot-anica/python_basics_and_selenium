# ---------- ВОЗВРАТ ОДНОГО ИЛИ НЕСКОЛЬКИХ ЗНАЧЕНИЙ
print("----- ВОЗВРАТ ОДНОГО ИЛИ НЕСКОЛЬКИХ ЗНАЧЕНИЙ -----")

# Возвращение одного значения
print("\nВозвращение одного значения")


def sum_numbers(x, y):
    return x + y


total = sum_numbers(3, 5)
print(total)  # 8

# Возвращение нескольких значений
print("\nВозвращение нескольких значений")


def personal_data(user_name, user_age, user_city):
    return user_name, user_age, user_city


name, age, city = personal_data("John", 25, "New York")
print(name)  # John
print(age)  # 25
print(city)  # New York
