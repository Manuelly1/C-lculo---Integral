from sympy import *

x = Symbol('x')

funcao = (4-(x**2))**(1/2) #o 1/2 no lugar da raiz

resultado = integrate((funcao),(x,0,2)).evalf()
print(resultado)