from sympy import *

x = Symbol('x')
funcao = sqrt(16 - x**2)

resultado = integrate(((funcao)),(x,0,4)).evalf()
print(resultado/4)