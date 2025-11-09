x, y = map(float, input("Введіть координати точки (x y): ").split())

if x > 0 and y > 0:
    print("Точка у I чверті")
elif x < 0 and y > 0:
    print("Точка у II чверті")
elif x < 0 and y < 0:
    print("Точка у III чверті")
elif x > 0 and y < 0:
    print("Точка у IV чверті")
elif x == 0:
    print("Точка знаходиться на осі Y")
elif y == 0:
    print("Точка знаходиться на осі X")