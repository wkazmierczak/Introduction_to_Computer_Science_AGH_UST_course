from math import sqrt



def czy_pierwsza(i):
    for y in range(2, int(sqrt(i))+1):
        if i % y == 0:
            return False
    return True


def suma_cyfr(i):
    suma = 0
    for x in str(i):
        suma += int(x)
    return suma


if __name__ == "__main__":
    i = 99999999999
    while True:
        if suma_cyfr(i) == 101 and czy_pierwsza(i):
            print(i)
            break
        i += 10000000

    #czy_pierwsza(31)