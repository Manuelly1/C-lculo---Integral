from sympy import *

x = Symbol('x')

funcao = sin(3*x)

resultado = integrate((funcao),(x,1,4)).evalf()
print(resultado)