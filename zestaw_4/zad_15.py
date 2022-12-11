from math import sqrt


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


def checking_if_every_has_prime_digit(num):
    while num > 0:
        digit = num % 10
        if is_prime(digit):
            return True
        num //= 10
    return False


def num_checking(T):
    l = len(T)
    for x in range(l):
        flag = True
        for y in range(l):
            if not checking_if_every_has_prime_digit(T[x][y]):
                flag = False
        if flag:
            return flag
    return False


if __name__ == '__main__':
    T = [
        [1, 2, 1, 4, 35],
        [1, 2, 3, 42, 25],
        [1, 2, 3, 7, 35],
        [12, 2, 3, 120, 200],
        [1, 2, 3, 300, 52],
    ]
    print(num_checking(T))