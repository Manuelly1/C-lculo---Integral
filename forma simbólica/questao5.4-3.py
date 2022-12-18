from sympy import *

x = Symbol('x')
numerador = (sin(x) - cos(x))
denominador = (sin(x) + cos(x))

resultado = integrate((((numerador/ denominador))**2*x+1),(x,1,pi/4)).evalf()
print(resultado)