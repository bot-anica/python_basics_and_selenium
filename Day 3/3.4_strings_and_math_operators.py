# ---------- STRINGS AND MATH OPERATORS
print("----- STRINGS AND MATH OPERATORS -----")

print("Happy" + " " + "Birthday")
print("Happy" * 3)

print(f'{"-" * 20}\nHappy Birthday\n{"-" * 20}\n\n')

# Индексы, строки и срезы
print("Happy Birthday"[0])  # H
print("Happy Birthday"[0:4])  # Happ
print("Happy Birthday"[0:5:2])  # Hpy
print("Happy Birthday"[::-1])  # yadhtriB yppaH

word = input("Enter a word and I will check if it's a palindrome: ").lower()

print(f'"{word}" is a palindrome: {word == word[::-1]}')
