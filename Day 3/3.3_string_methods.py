# def show_string_differences(string, new_string):
#     print(f"Was: {string}\n"
#           f"Now: {new_string=}\n"
#           f"{"-" * 20}\n\n")


# ---------- STRING METHODS MAIN
print("----- STRING METHODS MAIN -----")

# Методы строк

# upper() - переводит все символы в верхний регистр
# lower() - переводит все символы в нижний регистр
# title() - переводит первый символ в верхний регистр
# capitalize() - переводит первый символ в верхний регистр
# split() - разбивает строку на подстроки
# join() - объединяет подстроки в строку
# replace() - заменяет подстроку в строке
# strip() - удаляет пробелы в начале и в конце строки

song_title = " Happy Birthday To You  "

print(song_title.upper())
print(song_title.lower())
print(song_title.title())
print(song_title.strip().capitalize())
print(song_title.split())
print(" ".join(song_title.split()))  # WARNING !!! ВНИМАНИЕ !!!
print(song_title.replace("Happy", "Sad"))
print(song_title.strip())

# ---------- STRING METHODS ADDITIONAL
print("\n----- STRING METHODS ADDITIONAL -----")

# find() - ищет подстроку в строке и возвращает индекс первого вхождения, если подстрока не найдена возвращает -1
# index() - ищет подстроку в строке и возвращает индекс первого вхождения, если подстрока не найдена возвращает ошибку
# count() - подсчитывает количество вхождений подстроки
# len() - возвращает длину строки
# startswith() - проверяет, начинается ли строка с указанной подстроки
# endswith() - проверяет, заканчивается ли строка с указанной подстроки
# isalpha() - проверяет, состоит ли строка только из букв
# isdigit() - проверяет, состоит ли строка только из цифр
# isalnum() - проверяет, состоит ли строка только из букв и цифр
# islower() - проверяет, состоит ли строка только из нижнего регистра
# isupper() - проверяет, состоит ли строка только из верхнего регистра
# isnumeric() - проверяет, состоит ли строка только из цифр

print(song_title.lower().find("happy"))
print(song_title.index("Happy"))
print(song_title.count("Happy"))
print(len(song_title))
print(song_title.startswith("Happy"))
print(song_title.endswith("Happy"))
print(song_title.isalpha())
print(song_title.isdigit())
print(song_title.isalnum())
print(song_title.islower())
print(song_title.isupper())
print(song_title.isnumeric())
