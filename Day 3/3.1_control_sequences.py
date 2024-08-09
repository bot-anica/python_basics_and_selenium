# ---------- УПРАВЛЯЮЩИЕ ПОСЛЕДОВАТЕЛЬНОСТИ
print("----- CONTROL SEQUENCES -----")

# \n - перевод строки
# \t - табуляция
# \' - одинарная кавычка
# \" - двойная кавычка
# \\ - обратный слеш

print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\'World")
print("Hello\"World")
print("Hello\\World")

# ---------- INPUT & OUTPUT FUNCTIONS
print("\n----- INPUT & OUTPUT FUNCTIONS -----")

# input() - ввод данных
# print() - вывод данных

name = input("Enter your name: ")
print(f"Hello, {name}! How are you?")

# sep - разделитель
# end - окончание

name = input("Enter your name: ")
print(f"Hello", name, sep=", ", end="! ")
print("How are you?")
