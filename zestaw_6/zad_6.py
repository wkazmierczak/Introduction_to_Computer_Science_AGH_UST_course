# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10

# wartosci
# 3 + 5 + 2 = 10
# indeksy
# 2 + 3 + 5 = 10

def zad_6(T, suma_ind=0, suma_wart=0, i=0):
    if suma_ind == suma_wart != 0:
        return suma_ind

    if i == len(T):
        return 0

    return zad_6(T, suma_ind + i, suma_wart + T[i], i + 1) or zad_6(T, suma_ind, suma_wart, i + 1)


if __name__ == '__main__':
    T = [2, 7, 2, 5, 11, 2]
    print(zad_6(T))
