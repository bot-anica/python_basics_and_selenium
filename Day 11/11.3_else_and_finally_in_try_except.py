# ---------- ELSE AND FINALLY IN TRY/EXCEPT
print("----- ELSE AND FINALLY IN TRY/EXCEPT -----")

# try - попытка выполнить код
# except - если возникает ошибка
# else - если не возникает ошибки
# finally - в любом случае

# ---------- ПРИМЕРЫ ----------
print("----- ПРИМЕРЫ -----")

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    res = first_number / second_number
except ValueError:
    print("You must enter a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
finally:
    print("Thanks for using this app!")
