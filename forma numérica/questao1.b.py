from math import*


def funcao(x):
    return 1 / (x*(x+1)**2)


def formaTrapezio(f,a, b, N):
    h = (b-a)/N
    soma = 0
    for k in range(1, N):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

a = 1
b = 2
N = 1000

r = formaTrapezio(funcao,a,b,N)
print(r)