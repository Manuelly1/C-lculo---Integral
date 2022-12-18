from sympy import *

x = Symbol('x')

funcao = (x + 4)**(1/2)

resultado = integrate((funcao),(x,-1,4)).evalf()
print(resultado)