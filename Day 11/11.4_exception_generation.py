# ---------- EXCEPTION GENERATION
print("----- EXCEPTION GENERATION -----")

# raise - генерирует исключение

student_mark = input("Enter student mark between 0 and 10: ")

try:
    if student_mark.isnumeric():
        student_mark = int(student_mark)
    else:
        raise ValueError("You must enter a number!")  # raise - генерирует исключение

    if student_mark < 0 or student_mark > 10:
        raise ValueError("You must enter a number between 0 and 10!")  # raise - генерирует исключение
except ValueError as ve:
    print(ve)
else:
    print(f"Your mark is {student_mark}")
