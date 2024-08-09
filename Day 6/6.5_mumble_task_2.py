# ---------- MAMBLE TASK 2
print("----- MUMBLE TASK -----")

BAD_LETTER = "r"
THRESHOLD = 3

user_input = input("Enter a few words separated by a space for check: ").lower().split(" ")

bad_words = []

for word in user_input:
    bad_letter_count = word.count(BAD_LETTER)  # count() - counts the number of occurrences of a substring in a string
    if bad_letter_count >= THRESHOLD:
        bad_words.append(word)

if len(bad_words) == 0:
    print(f'Your input are good. It doesn\'t have words that contain more than "{THRESHOLD - 1}" "{BAD_LETTER}"')
else:
    print(f'Your input are bad. '
          f'It has {len(bad_words)} words that contain more than "{THRESHOLD - 1}" "{BAD_LETTER}":')

    for index, word in enumerate(bad_words, start=1):
        print(f"{index}. {word}")
