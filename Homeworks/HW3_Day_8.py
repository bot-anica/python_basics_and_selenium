# Генератор пословиц
import random
from HW3_Day_8_data import proverbs, variants

# Условия задачи 📒
# 1. Вне цикла объявите запрос, сколько пользователь хочет получить пословиц.
# 2. Вне цикла объявляете пустой список для результатов
# 3. Объявите цикл в котором вы будете добывать
# Случайный элемент из списка пословиц (добыли - удалили)
# Случайный элемент из списка вариантов замены (добыли - удалили)
# 4. Заменяете слово ум в добытой пословице на случайное существительное, добытое ранее
# 5. Добавляете сгенерированную пословицу в список
# 6. Цикл делаете до тех пор, пока в списке не будет заказанное в п.1 количество пословиц!
# 7. Выведите результат на экран

proverbs_len = len(proverbs)
variants_len = len(variants)

def get_wished_quotes_quantity():
    wished_quotes_quantity = input(f"How many quotes do you want (max {variants_len})? ")

    if wished_quotes_quantity.isnumeric():
        wished_quotes_quantity = int(wished_quotes_quantity)

        if wished_quotes_quantity > variants_len:
            print(f"Please enter a number less or equal than {variants_len}")
            return get_wished_quotes_quantity()
        
        return wished_quotes_quantity
    else:
        print("Please enter a number")
        return get_wished_quotes_quantity()


user_wished_quotes_quantity = get_wished_quotes_quantity()
results = []

for i in range(user_wished_quotes_quantity):
    random_proverb = proverbs.pop()
    random_variant = variants.pop()

    results.append(random_proverb.replace("Ум", random_variant.title()))

    proverbs_len -= 1
    variants_len -= 1

print(results)
