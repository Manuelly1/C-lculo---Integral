from sympy import *

x = Symbol('x')

funcao = sin(3*x)*cos(x) 

resultado = integrate((funcao),(x,0,pi/2)).evalf()
print(resultado)