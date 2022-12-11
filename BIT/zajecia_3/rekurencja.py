from math import sqrt


def waga(T, M, i=0):
    l = len(T)
    if M == 0:
        return True
    if i == l:
        return False
    return waga(T, M - T[i], i+1) or waga(T, M, i+1)


def fib_dyskretna(n):
    l = n-1
    return int((1/sqrt(5))*(((1+sqrt(5))/2)**(l+1)-((1-sqrt(5))/2)**(l+1)))


def fib_rek(n, licznik = 0):
    licznik += 1
    if n <= 2:
        return licznik
    return fib_rek(n-1) + fib_rek(n-2)


if __name__ == '__main__':
    T = [20, 20, 20, 20, 20, 1]
    print(fib_rek(10))
    print(fib_dyskretna(10))