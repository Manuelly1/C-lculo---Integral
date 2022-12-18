from sympy import *

x = Symbol('x')

funcao = x / sqrt(x**2 + 9)

resultado = integrate((funcao),(x,0,3)).evalf()
print(resultado)