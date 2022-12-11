# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.

from random import randint


def zad_21(T, suma, col=0):
    if suma == 0:
        return True
    if col == len(T):
        return False
    for row in range(len(T)):
        if row == col:
            continue
        return zad_21(T, suma - T[row][col], col + 1) or zad_21(T, suma, col + 1)


if __name__ == '__main__':
    T_1 = [[randint(1, 100) for _ in range(8)] for _ in range(8)]
    T = [[1, 2, 3, 2],
         [1, 2, 3, 2],
         [1, 2, 3, 2],
         [1, 2, 3, 2],
         ]
    for t in T:
        print(t)
    print(zad_21(T, 10))
