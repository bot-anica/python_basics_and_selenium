# ---------- IF, ELIF and STRING OPERATOR IN
print("----- IF, ELIF and STRING OPERATOR IN -----")

# in - проверяет наличие подстроки в строке

film_description = ("Main hero is usual employee of the IT company. "
                    "Every day he works and every day he makes a profit. "
                    "Once a year he goes on vacation. This year is not an exceptional one. "
                    "He is going to spend some time for traveling.")

if "driving" in film_description:
    print("This film about driving")
elif "IT" in film_description:
    print("This film about IT company or about some IT employee")
elif "fighting" in film_description:
    print("This film about fighting")
else:
    print("I don't know this film")
