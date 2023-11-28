from math import sqrt


def komnaty(T, szt=0, i=0):
    if i == len(T) - 1:
        return T[i] + szt < 100 and is_prime(T[i] + szt)
    for zmiana in range(szt - 6, szt + 1):
        if is_prime(T[i] + zmiana) and T[i] + zmiana < 100:
            T[i] += zmiana
            if komnaty(T, szt - zmiana, i+1):
                return True

    return False


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 3 == 0 or num % 2 == 0 or num < 2:
        return False
    i = 5
    while i < sqrt(num) + 1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


if __name__ == '__main__':
    T = [10, 20, 35]
    print(komnaty(T))
