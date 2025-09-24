a = int(input("Скільки чисел у масиві? "))
b = []
c = 0
while c < a:
    x = int(input("Введіть число: "))
    b.append(x)
    c = c + 1
print("Ваш масив:", b)

k = int(input("Введіть k: "))
c = 0
while c < len(b):
    b[c] = b[c] + k
    c = c + 1
print("Масив після збільшення:", b)