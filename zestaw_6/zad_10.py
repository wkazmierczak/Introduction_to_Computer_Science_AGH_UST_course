from random import randint


def wyznacznik_macierzy(macierz, iloczyn=1):
    # printowanie_macierzy(macierz)
    # print(iloczyn)
    if len(macierz) == 1:
        return macierz[0]
    if len(macierz) == 2:
        return round(iloczyn*(macierz[0][0]*macierz[1][1]-macierz[0][1]*macierz[1][0]), 2)
    else:
        nowa_macierz, div = zerowanie_pierwszej_kolumny(macierz)
        return wyznacznik_macierzy(nowa_macierz, iloczyn*div)


def zerowanie_pierwszej_kolumny(macierz):
    best_row = 0
    size = len(macierz)
    for row in range(size):
        if macierz[row][0] != 0:
            best_row = row
        if macierz[row][0] == 1:
            best_row = row
            break

    for row in range(size):
        if row == best_row:
            continue
        div = macierz[row][0] / macierz[best_row][0]
        for col in range(size):
            macierz[row][col] -= div*macierz[best_row][col]

    for row in range(size):
        macierz[row] = macierz[row][1:size]
    macierz.pop(best_row)

    if size == 3:
        return macierz, (-1)**best_row
    else:
        return macierz, macierz[best_row][0] * (-1) ** best_row


def printowanie_macierzy(macierz):
    for line in macierz:
        print(line)
    print("\n")


if __name__ == '__main__':
    size = randint(3, 5)
    macierz_1 = [[randint(0, 9) for _ in range(size)]for _ in range(size)]
    macierz =[[1,-1,2,4],
              [0,1,0,3],
              [5,7,-2,0],
              [2,0,-1,4]]

    macierz_2 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]

    # printowanie_macierzy(macierz)
    #
    # printowanie_macierzy(zerowanie_pierwszej_kolumny(macierz)[0])

    print(wyznacznik_macierzy(macierz))