from sympy import *

#sem intervalo
x = Symbol('x')
numerador = (sin(x)**2 - 4*sin(x) * cos(x) + 3*cos(x)**2)
denominador = (sin(x) + cos(x))

resultado = integrate(((numerador/denominador)),(x)).evalf()
print(resultado)