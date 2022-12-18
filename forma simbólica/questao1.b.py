from sympy import *

x = Symbol('x')
funcao = 1 / (x*(x+1)**2)

resultado = integrate((funcao),(x,1,2)).evalf()
print(resultado)