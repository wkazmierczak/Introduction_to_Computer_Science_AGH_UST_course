from math import sqrt


def is_prime(num):
    if num ==2 or num ==3:
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


def num_has_every_digit_prime(num):
    while num > 0:
        digit = num % 10
        if not is_prime(digit):
            return False
        num //= 10
    return True


def row_checking(T):
    l = len(T)
    for x in range(l):
        a = False
        for y in range(l):
            if num_has_every_digit_prime(T[x][y]):
                a = True
        if not a:
            return False
    return True


if __name__ == '__main__':
    T = [
        [1, 22, 3, 4, 5],
        [1, 22, 3, 4, 5],
        [1, 1, 22, 300, 8],
        [1, 22, 3, 100, 200],
        [1, 2, 3, 4, 5],
    ]
    print(row_checking(T))