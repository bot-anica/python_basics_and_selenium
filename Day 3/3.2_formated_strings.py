# ---------- FORMATED STRINGS
print("----- FORMATED STRINGS -----")

# f - форматированный строк

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = float(input("Enter your height: "))
# isMarried = bool(int(input("Are you married? (1/0): ")))
#
# print("My name is " + name + " and I am " + str(age) + " years old. My height is " + str(height) + " m. I am " + str(isMarried))
# print(f"My name is {name} and I am {age} years old. My height is {height} m. I am {isMarried}")

# ---------- DEBUGGER PRINT
print("\n----- DEBUGGER PRINT -----")

name = "John"
age = 30

print(f"name:", name)
print(f"age:", age)

# OR

print(f"{name=}")
print(f"{age=}")

# ---------- R-STRING
print("\n----- R-STRING -----")

# Спецсимволы не обрабатываются
# Позволяют отключать экранирование
# Позволяют писать регулярные выражения
# Позволяют писать пути к файлам
# Позволяют писать HTML-код
# Позволяют писать SQL-запросы
# Позволяют писать JSON-код
# Позволяют писать XML-код
# Позволяют писать CSS-код

row_string_path = r"C:\Users\...\file.txt"
row_string_html = "<html><body>Hello, World!</body></html>"
row_string_sql = "SELECT * FROM table WHERE id = 1"
row_string_json = '{"name": "John", "age": 30}'
row_string_xml = "<employee><name>John</name><age>30</age></employee>"
row_string_css = "body { color: red; }"

print(row_string_path)
print(row_string_html)
print(row_string_sql)
print(row_string_json)
print(row_string_xml)
print(row_string_css)

# ---------- RF-STRING
print("\n----- RF-STRING -----")

name = "John"
age = 30

print(f"Имя: {name};\nВозраст: {age=};")
print(rf"Имя: {name};\nВозраст: {age=};")  # \n и подобные спецсимволы не обрабатываются в RF-строках
