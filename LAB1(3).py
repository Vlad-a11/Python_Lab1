try:
    a = float(input("Ввелите a: "))
    b = float(input("Ввелите b: "))
    x = float(input("Ввелите x: "))
    try:
        if x < 6:
            y = 4*(x+a**2+b**2)
            print("Y = ", y)
        else:
            y = (6*x**2-a*b)/(2*x**2)
            print("Y = ", y)
    except:
        print("Нет решения")
except:
    print("Неверные вводные данные")
input("Нажмите Enter для выхода")