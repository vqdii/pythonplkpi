a = [5, 12, 0, 3, 25, 18, 40, 6, 55, 7, 10, 8]
for i in range(len(a)):
    if a[i] == 0:
        a[i] = -100
print(a)