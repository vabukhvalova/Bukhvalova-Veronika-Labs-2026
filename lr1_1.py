def vvod(name):
    while True:
        try:
            return float(input("Введите " + name + ": "))
        except ValueError:
            print("Это не число, введите число")


def vvesti_koef():
    a = vvod("A")
    b = vvod("B")
    c = vvod("C")
    return a, b, c


def reshenie_a_0(b, c):
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
            print("x =", t ** 0.5)
            print("x =", -t ** 0.5)


def reshenie(a, b, c):
    D = b * b - 4 * a * c
    print("D =", D)

    if D < 0:
        print("Корней нет")
    elif D == 0:
        t = -b / (2 * a)
        if t < 0:
            print("Корней нет")
        elif t == 0:
            print("x = 0")
        else:
            print("x =", t ** 0.5)
            print("x =", -t ** 0.5)
    else:
        t1 = (-b + D ** 0.5) / (2 * a)
        t2 = (-b - D ** 0.5) / (2 * a)

        if t1 > 0:
            print("x =", t1 ** 0.5)
            print("x =", -t1 ** 0.5)
        elif t1 == 0:
            print("x = 0")

        if t2 > 0:
            print("x =", t2 ** 0.5)
            print("x =", -t2 ** 0.5)
        elif t2 == 0:
            print("x = 0")

        if t1 < 0 and t2 < 0:
            print("Корней нет")


def main():
    a, b, c = vvesti_koef()
    if a == 0:
        reshenie_a_0(b, c)
    else:
        reshenie(a, b, c)


if __name__ == "__main__":
    main()