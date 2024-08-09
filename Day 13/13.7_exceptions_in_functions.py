# ---------- ИСКЛЮЧЕНИЯ В ФУНКЦИЯХ
print("----- ИСКЛЮЧЕНИЯ В ФУНКЦИЯХ -----")


def safe_divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("x and y must be numbers!")
        return None

    return result


division_result = safe_divide(5, 0)
print(f"{division_result}\n")

division_result = safe_divide(5, "a")
print(f"{division_result}\n")

division_result = safe_divide(5, 2)
print(f"{division_result}\n")

