a = int(input("Скільки чисел у масиві? "))

b = []
c = 0
while c < a:
    x = int(input("Введіть число: "))
    b.append(x)
    c = c + 1
print("Ваш масив:", b)

max = b[1]
c = 1
while c < len(b):
    if b[c] > max:
        max = b[c]
    c = c + 2

print("Максимальний елемент на непарній позиції:", max)