# ---------- FOR LOOP CONTROL OPERATORS
print("----- FOR LOOP CONTROL OPERATORS -----")

# break - прерывает цикл
# continue - пропускает текущую итерацию цикла и переходит к следующей
# else - выполняется после цикла

# Конструкция FOR-ELSE

welcome_message = "Hello, World!"
target_char = "l"

for char in welcome_message:
    if char.isnumeric():
        continue  # skip this iteration of the loop

    if char == target_char:
        print(f"Found '{target_char}' in '{welcome_message}'")
        break  # exit the loop
else:  # executed after the loop
    print(f"'{target_char}' not found in '{welcome_message}'")
