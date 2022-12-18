from sympy import *

x = Symbol('x')
numerador = (sin(x)**2 - sin(x) * cos(x) + 2*cos(x)**2)
denominador = (sin(x) + 2*cos(x))

resultado = integrate(((numerador/denominador)),(x)).evalf()
print(resultado)