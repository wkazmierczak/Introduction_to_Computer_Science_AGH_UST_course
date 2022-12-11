import random


def poszukiwanie_najdluzszego_ciagu_z_rewersem(tab):
    t1 = []
    naj_ciag = []
    longest = 0
    poczatek = 0
    while poczatek < len(tab):
        koniec = poczatek
        while koniec < len(tab):
            t1.append(tab[poczatek:koniec + 1])
            koniec += 1
        poczatek += 1
    for ciag in t1:
        if ciag[::-1] in t1:
            print(ciag[::-1])
            if len(ciag[::-1]) > longest:
                longest = len(ciag[::-1])
                naj_ciag = ciag[::-1]
    return longest, naj_ciag


if __name__ == '__main__':
    tab = [random.randint(1, 1000) for _ in range(100)]
    print(poszukiwanie_najdluzszego_ciagu_z_rewersem(tab))
