# ---------- GRADE
print("----- GRADE -----")

mark = input("Enter your mark: ")

if mark.isdigit():
    mark = int(mark)
else:
    print("Invalid mark")
    exit(1)

if 90 <= mark <= 100:
    print("A")
elif 80 <= mark < 90:
    print("B")
elif 70 <= mark < 80:
    print("C")
elif 60 <= mark < 70:
    print("D")
elif 0 <= mark < 60:
    print("F")
else:
    print("Invalid mark")
