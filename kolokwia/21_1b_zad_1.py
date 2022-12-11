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


def najw_iloczyn_pierwszych(tab):
    biggest_iloczyn = 1
    for indeks, num in enumerate(tab):
        iloczyn = 1
        for i in range(indeks):
            if is_prime(tab[i]):
                iloczyn *= tab[i]
        if iloczyn == num:
            if iloczyn > biggest_iloczyn:
                biggest_iloczyn = iloczyn
    if biggest_iloczyn == 1:
        return None
    else:
        return biggest_iloczyn


if __name__ == '__main__':
    tab = [1, 3, 4, 5, 15, 7, 105, 5]

    print(najw_iloczyn_pierwszych(tab))