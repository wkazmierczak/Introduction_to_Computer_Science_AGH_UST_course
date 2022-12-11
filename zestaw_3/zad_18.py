import random


def najdluzszy_ciag_palindrom_nieparzysty(tab):
    l = len(tab)
    longest = 0
    for x in range(l):
        for y in range(x + 1, l):
            flag = True
            for i in range(y - x + 1):
                if tab[x+i] != tab[y-i] or tab[x+i] % 2 == 0:
                    flag = False
                    break
            if flag:
                longest = max(longest, y - x + 1)
    return longest


if __name__ == '__main__':
    tab = [2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 3, 5, 3, 1]
    print(tab)
    print(najdluzszy_ciag_palindrom_nieparzysty(tab))