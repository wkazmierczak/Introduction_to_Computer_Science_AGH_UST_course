# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

def zad_32(T, dany, suma=0, suma_ind=0, i=0, counter =0):
    if suma == suma_ind and suma == dany:
        return True
    if i == len(T):
        return False
    return zad_32(T, dany, suma + T[i], suma_ind + i, i+1, counter) or zad_32(T, dany, suma, suma_ind, i+1, counter)
    


def wynik(t, dany):
    if zad_32(T, dany)>1:
        return True
    else:
        return False

T = [1, 2, 2, 1, 1, 1]
print(zad_32(T, 1))


