from math import sqrt


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num))+1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def czynniki_pierwsze(num):
    counter = 0
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                counter += 1
            while num % i == 0:
                num //= i
    return counter


def wagi(t, j=0, m=0, k=0, i=0):
    l = len(t)
    if j == m and m == k and i == l:
        return True
    if i == l:
        return False
    else:
        return wagi(t, j + czynniki_pierwsze(t[i]), m, k, i+1) or wagi(t, j, m + czynniki_pierwsze(t[i]), k, i+1)\
               or wagi(t, j, m, k + czynniki_pierwsze(t[i]), i+1)


if __name__ == '__main__':
    t = [5, 6, 2, 2, 3]
    print(wagi(t))
