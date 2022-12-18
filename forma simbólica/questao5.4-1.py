from sympy import *
print("Primeira questão da última página")

x = Symbol('x')

c = (x + 1) * sqrt(x**2 + 1)
y = 1 / c #função

resultado = integrate(y,(x, 0, 0.75)).evalf(5)
print(resultado)