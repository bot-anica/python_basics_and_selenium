# Константы
THRESHOLD_DIGITS = 1
THRESHOLD_UPPER = 1
THRESHOLD_LOWER = 1
THRESHOLD_LEN = 8

# Cчетчики для проверки
digit_counter = 0
upper_counter = 0
lower_counter = 0

input_password = input("Введите пароль: ")

password_length_is_valid = len(input_password) >= THRESHOLD_LEN

if password_length_is_valid:
    for char in input_password:
        if char.isnumeric():
            digit_counter += 1
        if char.isalpha():
            if char.islower():
                lower_counter += 1
            else:
                upper_counter += 1
else:
    print(f"Пароль '{input_password}' ненадежный")
    print(f"\tДлина пароля должна быть не менее {THRESHOLD_LEN} символов.")
    exit(1)

password_digit_count_is_valid = digit_counter >= THRESHOLD_DIGITS
password_upper_count_is_valid = upper_counter >= THRESHOLD_UPPER
password_lower_count_is_valid = lower_counter >= THRESHOLD_LOWER

if password_length_is_valid and password_digit_count_is_valid and password_upper_count_is_valid and password_lower_count_is_valid:
    print(f"Пароль '{input_password}' надежный.")
else:
    print(f"Пароль '{input_password}' ненадежный.")

    if not password_digit_count_is_valid:
        print(f"\tПароль должен содержать не менее {THRESHOLD_DIGITS} цифр.")
    if not password_upper_count_is_valid:
        print(f"\tПароль должен содержать не менее {THRESHOLD_UPPER} больших букв.")
    if not password_lower_count_is_valid:
        print(f"\tПароль должен содержать не менее {THRESHOLD_LOWER} маленьких букв.")
