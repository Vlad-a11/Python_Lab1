def reshenie(_a,_b,_x):

    if x < 6:
        _y = 4*(_x+_a**2+_b**2)
    else:
        _y = (6 * (_x ** 2) - _a * _b) / (2 * (_x ** 2))
    return _y
a = float(input("Ввелите a: "))
b = float(input("Ввелите b: "))
x = float(input("Ввелите x: "))

y = reshenie(a,b,x)
print("Y = ",y)
print(a)
input("Нажмите Enter для выхода")