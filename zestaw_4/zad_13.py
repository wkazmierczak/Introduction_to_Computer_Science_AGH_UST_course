from math import sqrt


def liczby_komplementarne(T):
    l = len(T)
    for x in range(l):
        for y in range(l):
            flag = False
            for a in range(l):
                for b in range(l):
                    if a == x and b == y:
                        continue
                    if is_prime(T[x][y]+T[a][b]):
                        flag = True
            if not flag:
                T[x][y] = 0
    return T


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num)) + 1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


if __name__ == '__main__':
    T = [
        [20, 20, 20, 20, 20],
        [20, 20, 20, 20, 5],
        [20, 20, 27, 20, 20],
        [20, 2, 20, 20, 20],
        [20, 20, 20, 20, 1],
    ]

    print(liczby_komplementarne(T))