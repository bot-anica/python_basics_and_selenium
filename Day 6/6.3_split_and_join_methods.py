# ---------- SPLIT AND JOIN METHODS
print("----- SPLIT AND JOIN METHODS -----")

# split() - разбивает строку на подстроки и возвращает их в виде списка
# join() - объединяет список подстрок в строку

user_marks = input("Enter your marks for last 3 months: ").split()
print(user_marks)

results = []

for mark in user_marks:
    if mark.isdigit():
        mark = int(mark)
        if 0 < mark <= 5:
            results.append(mark)

        if mark == 5:
            print("Good")
        elif mark == 4:
            print("Satisfactory")
        elif mark == 3:
            print("Not good")
        elif mark == 2:
            print("Bad")
        elif mark == 1:
            print("Awful")
        else:
            print("Invalid mark")
    else:
        print("You entered not a number")
        print("You have to enter numbers from 1 to 5")
        break
else:
    print(f"Your marks: {results}")
    print(f"Average mark: {sum(results) / len(results):.2f}")