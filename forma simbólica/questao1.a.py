from sympy import *

x = Symbol('x') #definindo o x de forma simbólica

funcao = (2*x + 1) / sqrt(5*x - 1) 

resultado = integrate((funcao),(x,0,1)).evalf()
print(resultado)