from math import sqrt


def rozne_cyfry(num):
    tab = [0 for _ in range(10)]
    while num > 0:
        digit = num % 10
        if tab[digit] == 0:
            tab[digit] += 1
        else:
            return False
        num //= 10
    return True


def najwieksza_pierwsza_z_odcietych(k):
    biggest = 0
    while k > 0:
        n = 0
        i = 1
        while n < k:
            n = k % (10**i)
            if is_prime(n) and rozne_cyfry(n):
                biggest = max(biggest, n)
            i += 1
        k //= 10
    return biggest


def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


if __name__ == '__main__':
    print(najwieksza_pierwsza_z_odcietych(1202742516))