def sequence(T):
    l = len(T)
    podciagi = [[] for _ in range(l // 2)]
    poczatek = 0
    koniec = 0
    i = 0

    while poczatek < l:
        while koniec + 1 < l:
            if T[koniec + 1] < T[koniec]:
                if len(T[poczatek:koniec + 1]) > 2:
                    podciagi[i] = T[poczatek:koniec + 1]
                    i += 1
                poczatek = koniec + 1
                koniec = poczatek
                break
            koniec += 1
        else:
            poczatek += 1

    for x in range(i):
        for y in range(i):
            if x == y:
                continue
            if podciagi[x][-1] < podciagi[y][0]:
                return True
    return False


if __name__ == '__main__':
    T = [2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]
    print(sequence(T))

