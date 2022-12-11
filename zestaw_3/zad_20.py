from math import sqrt


def czy_pierwsza(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num < 2:
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


def podzial_na_czynniki_pierwsze(tab):
    tab_czynnikow = []
    biggest = 0
    longest = 0
    x = []
    counter = 0

    for num in tab:
        a = True
        i = 2
        while i < num + 1 and a:
            while num % i == 0 and czy_pierwsza(i):
                if i in tab_czynnikow:
                    if counter > longest:
                        longest = counter
                    counter = 0
                    tab_czynnikow.clear()
                    a = False
                else:
                    tab_czynnikow.append(i)
                    num //= i
                    if num == 1:
                        counter += 1
            if counter > longest:
                longest = counter
            i += 1
    return longest


if __name__ == '__main__':
    print(podzial_na_czynniki_pierwsze([2, 23, 33, 5, 7, 13, 17, 7, 5, 11, 13, 22]))
