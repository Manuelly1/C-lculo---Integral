from sympy import *

x = Symbol('x')

funcao = sin(x)**2

resultado = integrate((funcao),(x,0,pi/2)).evalf()
print(resultado)