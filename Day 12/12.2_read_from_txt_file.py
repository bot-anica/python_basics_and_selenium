# ---------- READ FROM TXT FILE
print("----- READ FROM TXT FILE -----")

# Открыть файл для чтения.
# Если файл не существует, то получим ошибку FileNotFoundError.
# Используется флаг "r".
with open("hello.txt", "r", encoding="utf-8") as file:
    print(file.read())  # file.read() - читает содержимое файла целиком

with open("hello.txt", "r", encoding="utf-8") as file:
    print(file.readlines())  # file.readlines() - читает содержимое файла построчно
