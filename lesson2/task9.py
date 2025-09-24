a = int(input("Скільки чисел у масиві? "))
b = []
c = 0
while c < a:
    x = int(input("Введіть число: "))
    b.append(x)
    c = c + 1
print("Ваш масив:", b)
b.pop()
print("Масив після видалення останнього елемента:", b)