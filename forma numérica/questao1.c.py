from math import*

def funcao(x):
    return x / sqrt(x**2 + 9)


def metodo_trapezio(f,a, b, N):
    h = (b-a)/N
    soma = 0
    for k in range(1, N):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

a = 0
b = 3
N = 1000

r = metodo_trapezio(funcao,a,b,N)
print(r)
