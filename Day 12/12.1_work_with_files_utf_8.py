# ---------- РАБОТА С ФАЙЛАМИ: UTF-8
print("----- РАБОТА С ФАЙЛАМИ: UTF-8 -----")

english_text = "Hello, World!"
russian_text = "Привет, Мир!"

byte_string_english_utf8 = english_text.encode("UTF-8")
byte_string_russian_utf8 = russian_text.encode("UTF-8")

byte_string_english_windows1251 = english_text.encode("Windows-1251")
byte_string_russian_windows1251 = russian_text.encode("Windows-1251")

byte_string_english_ascii = english_text.encode("ASCII")

print(byte_string_english_utf8)
print(byte_string_russian_utf8)

print(byte_string_english_windows1251)
print(byte_string_russian_windows1251)

print(byte_string_english_ascii)
