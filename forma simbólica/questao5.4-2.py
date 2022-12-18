from sympy import *

x = Symbol("x")

print(float(integrate(asin(sqrt(x))/(sqrt(x*(1 - x))),(x,0,1))))