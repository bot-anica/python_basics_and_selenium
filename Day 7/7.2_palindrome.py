# ---------- PALINDROME
print("----- PALINDROME -----")

while True:
    user_input = input("Enter a few words: ").lower().split(" ")

    if user_input == [""]:
        break

    while user_input:
        word = user_input.pop(0)
        if word == word[::-1]:
            print(word, "is a palindrome")
        else:
            print(word, "is not a palindrome")
