# ---------- CONDITIONAL STATEMENTS
print("----- CONDITIONAL STATEMENTS -----")

num = 5

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

# ---------- TERNARY OPERATOR
print("\n----- TERNARY OPERATOR -----")

num = 5
min = 1
max = 10

print("Number is in range" if min <= num <= max else "Number is out of range")