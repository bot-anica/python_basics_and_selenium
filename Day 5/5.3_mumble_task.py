# ---------- MUMBLE TASK
print("----- MUMBLE TASK -----")

BAD_LETTER = "r"
THRESHOLD = 3

word = input("Enter a word for check: ")
r_char_counter = 0

for char in word:
    if char.lower() == BAD_LETTER:
        r_char_counter += 1
        if r_char_counter == THRESHOLD:
            print(f'That\'s three "{BAD_LETTER}" in your word. Don\'t make fun of me!')
            break
        else:
            print(f'There\'s an "{BAD_LETTER}" in there, but it\'s tolerable for now')
else:
    if r_char_counter == 0:
        print(f'Word is great. It doesn\'t have "{BAD_LETTER}" in it')
    else:
        print(f'Word is good. It has only {r_char_counter} "{BAD_LETTER}" in it')
