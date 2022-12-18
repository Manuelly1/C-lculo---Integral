from sympy import *

x = Symbol('x')

funcao = sqrt(3*x + 5)

resultado = integrate((funcao),(x,0,2)).evalf()
print(resultado)