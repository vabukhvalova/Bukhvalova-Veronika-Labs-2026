while True:
    try:
        a = float(input("Введите A: "))
        break
    except ValueError:
        print("Это не число, введите число")

while True:
    try:
        b = float(input("Введите B: "))
        break
    except ValueError:
        print("Это не число, введите число")

while True:
    try:
        c = float(input("Введите C: "))
        break
    except ValueError:
        print("Это не число, введите число")

if a == 0:
    if b == 0:
        if c == 0:
            print("Уравнение 0 = 0, любое x является решением")
        else:
            print("Уравнение не имеет решений")
    else:
        t = -c / b
        if t < 0:
            print("Нет действительных корней")
        elif t == 0:
            print("x = 0")
        else:
            x1 = t ** 0.5
            x2 = -x1
            print("x1 =", x1)
            print("x2 =", x2)
else:
    D = b * b - 4 * a * c
    print("D =", D)

    if D < 0:
        print("Нет действительных корней")
    elif D == 0:
        t = -b / (2 * a)
        if t < 0:
            print("Нет действительных корней")
        elif t == 0:
            print("x = 0")
        else:
            x1 = t ** 0.5
            x2 = -x1
            print("x1 =", x1)
            print("x2 =", x2)
    else:
        t1 = (-b - D ** 0.5) / (2 * a)
        t2 = (-b + D ** 0.5) / (2 * a)

        if t1 > 0:
            x1 = t1 ** 0.5
            x2 = -x1
            print("x1 =", x1)
            print("x2 =", x2)
        elif t1 == 0:
            print("x = 0")

        if t2 > 0:
            x3 = t2 ** 0.5
            x4 = -x3
            print("x3 =", x3)
            print("x4 =", x4)
        elif t2 == 0:
            print("x = 0")

        if t1 < 0 and t2 < 0:
            print("Нет действительных корней")