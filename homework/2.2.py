a= int(input("Введіть ширину (a): "))
b = int(input("Введіть висоту (b): "))
c = input("Введіть символ для контуру (c): ")
d = input("Введіть символ для заливки (d): ")

if c == "": c = "X"
if d == "": d = " "

if a <= 0 or b <= 0:
    print("Ширина і висота більше 0")
else:
    if b == 1:
        print(c * a)
    elif a == 1:
        for _ in range(b):
            print(c)
    else:
        print(c * a)
        for _ in range(b - 2):
            print(c + d * (a - 2) + c)
        print(c * a)
