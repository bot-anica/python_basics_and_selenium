# ---------- ФУНКЦИИ
print("----- ФУНКЦИИ -----")

# Функция - это набор определенных действий, которые могут выполняться в программе


a = 5
b = 10

# Пример кода без функций

# Сложение двух чисел
total_1 = a + b

# Умножение двух чисел
total_2 = a * b

print(total_1, total_2)


# Пример кода с использованием функций
def sum_numbers(x, y):
    return x + y


def multiply_numbers(x, y):
    return x * y


total_1 = sum_numbers(3, 5)
total_2 = multiply_numbers(7, 8)

print(total_1, total_2)
