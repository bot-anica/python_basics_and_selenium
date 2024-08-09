# ---------- CONDITIONAL STATEMENTS AND LOGICAL OPERATORS
print("----- CONDITIONAL STATEMENTS AND LOGICAL OPERATORS -----")

x = 5
y = 10

if x > 0 and y > 0:
    print("Both numbers are positive")
else:
    print("At least one number is not positive")

if x > 0 or y > 0:
    print("At least one number is positive")
else:
    print("Both numbers are not positive")


# ---------- TERNARY OPERATOR
print("\n----- TERNARY OPERATOR -----")

x = 5
y = 10

print("Both numbers are positive" if x > 0 and y > 0 else "At least one number is not positive")
print("At least one number is positive" if x > 0 or y > 0 else "Both numbers are not positive")


userName = input("Enter your user name: ")

if userName.isalpha():
    print("User name contains only letters")
elif userName.isnumeric():
    print("User name contains only numbers")
else:
    print("User name contains letters and numbers")
