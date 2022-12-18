from sympy import *

x = Symbol('x')

funcao = x**5

resultado = integrate((funcao),(x,1,5)).evalf()
print(resultado)