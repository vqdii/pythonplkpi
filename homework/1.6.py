age = int(input("Введіть свій вік: "))

if age < 0 or age > 120:
    print(" вік")
else:
    if age % 10 == 1 and age % 100 != 11:
        word = "рік"
    elif age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        word = "роки"
    else:
        word = "років"
    print(f"{age} {word}")
