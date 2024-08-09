# Вам пришло секретное послание.
# Оно содержит много странных символов, которые вы не можете понять.
# Но вы знаете, что в этом послании используются только маленькие русские буквы.
# Так же, в каждом вложенном списке, содержится только одно слово.
# Используйте знание языка Python а так же знание for i чтобы расшифровать его.

# Секретное послание
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
                 ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'],
                 ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
                 ['и$ sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
                 ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

# Список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
             'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Вот что у меня получилось
words = []

for secret_word in secret_letter:
    usual_word_chars = ''

    for secret_char in secret_word[0]:
        if small_rus.count(secret_char):
            usual_word_chars += secret_char

    words.append("".join(usual_word_chars))
else:
    print(" ".join(words))
