# ---------- WHILE LOOP
import random

print("----- WHILE LOOP -----")

number = 0
while number < 5:
    print(number)
    number += 1

# Control loop operators
# break
# continue

print("\n BREAK")
number = 0
while number < 5:
    number += 1
    if number == 3:
        break  # прерывает цикл
    print(number)

print("\n CONTINUE")
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue  # пропускает текущую итерацию цикла и переходит к следующей
    print(number)

# Infinite loop
print("\n INFINITE LOOP")
right_answer = random.randint(1, 10)
continue_asking = True

while continue_asking:
    user_answer = int(input("Enter a number from 1 to 10: "))

    if user_answer == right_answer:
        print("You are right!")
        continue_asking = False
    else:
        print("You are wrong!")
else:
    print(f"\nThe right answer is {right_answer}\n")
