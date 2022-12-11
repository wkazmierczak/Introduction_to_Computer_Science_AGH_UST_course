# Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
# o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
# która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
# -1.

from math import sqrt

def zad_25(T, i=0):
    if i == len(T)-1:
        return True
    if i > len(T)-1:
        return False
    pierwsze = pierwsze(T[i])
    for k in pierwsze:
        if mozna(T, pierw):
            zad_25(T, i+k)


# def mozna(T, num):
#     if 

def pierwsze(num):
    tab = []
    div = 2
    while num > 0:
        if num % div == 0:
            tab.append(div)
            while num % div:
                num /= div
        div += 1
    return tab

print(pierwsze(4))