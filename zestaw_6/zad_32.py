# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.



def zad_32(T, dany, flag, suma_1=0, suma_2=0, i=0):
    global flag_1
    if suma_1 == suma_2:
        return True
    if i == len(T):
        return False
    return zad_32(T, dany, True, suma_1 + T[i], suma_2, i+1) or zad_32(T, dany, True, suma_1, suma_2 +T[i], i+1)


T = [1, 2, 2, 1, 1, 1]
print(zad_32(T, 1, False))


