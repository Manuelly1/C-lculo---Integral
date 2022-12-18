from math import*

def funcao(x):
    return sqrt(4 - x**2)


def metodo_trapezio(f,a, b, N):
    h = (b-a)/N
    soma = 0
    for k in range(1, N):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

a = 0
b = 2
N = 1000

r = metodo_trapezio(funcao,a,b,N)
print(r)

