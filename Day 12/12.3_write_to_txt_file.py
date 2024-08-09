# ---------- WRITE TO TXT FILE
print("----- WRITE TO TXT FILE -----")

# Использование функции open()

# open(filename, mode='r', encoding=None)

# - filename - имя файла
# - mode - режим работы:
#     'r' - open for reading (default)
#     'w' - open for writing, truncating the file first
#     'x' - create a new file and open it for writing
#     'a' - open for writing, appending to the end of the file if it exists
#     'b' - binary mode
#     't' - text mode (default)
#     '+' - open a disk file for updating (reading and writing)
# Моды могут комбинироваться, например:
#     'w+b' - открыть для записи и для двоичного режима
#     'r+' - открыть для чтения и для записи
#     'a+' - открыть для чтения и для дозаписи
#     'r+b' - открыть для чтения и для двоичного режима
# - encoding - кодировка

# Открыть файл для записи.
# Если файл не существует, он будет создан.
# Если он уже существует, то он будет перезаписан.
# Используется флаг "w".
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")

# Открыть файл для дозаписи.
# Если файл не существует, он будет создан.
# Если он уже существует, то он будет дозаписан.
# Используется флаг "a".
with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("Привет, Мир!\n")
