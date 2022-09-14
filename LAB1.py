a = float(input("Ввелите a: "))
b = float(input("Ввелите b: "))
x = float(input("Ввелите x: "))
if x < 6:
    y = 4*(x+a**2+b**2)
    print("Y = ", y)
else:
    y = (6*(x**2)-a*b)/(2*(x**2))
    print("Y = ", y)
input("Нажмите Enter для выхода")