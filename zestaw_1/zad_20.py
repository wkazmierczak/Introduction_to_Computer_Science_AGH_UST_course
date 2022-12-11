from math import sqrt


def fun(a, b):
    eps = 10e-6
    while abs(a - b) > eps:
        a, b = sqrt(a*b), (a+b)/2
    return (a+b)/2


print(fun(45, 5))