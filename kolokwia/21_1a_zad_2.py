def konwerter_na_sys_o_podst_4(num):
    t_1 = [False for _ in range(4)]
    #suma = 0
    #i = 0
    while num > 0:
        digit = num % 4
        num //= 4
        t_1[digit] = True
        #suma = digit*(10**i) + suma
        #i += 1
    #return suma
    return t_1


def najdluzszy_podciag(tab):
    poczatek = 0
    koniec = 0
    longest = 0
    while poczatek < len(tab):
        counter = 0
        koniec = poczatek
        while koniec < len(tab):
            if konwerter_na_sys_o_podst_4(tab[poczatek]) == konwerter_na_sys_o_podst_4(tab[koniec]):
                counter += 1
            koniec += 1
        if counter > longest:
            longest = counter
        poczatek += 1
    return longest


if __name__ == '__main__':
    tab = [13, 107, 107, 57, 31, 13, 31]
    print(najdluzszy_podciag(tab))