a = [5, 12, 0, -3, 25, 18, 40, -6, 55, 7, 10, -8]
b = 1
for i in a:
    if i < 0:
        b *= i
print(b)