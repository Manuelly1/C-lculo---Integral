from sympy import *

x = Symbol('x')

funcao = x*(x**2 - 1)**4 

resultado = integrate((funcao),(x,1,2)).evalf()
print(resultado)