def dzielniki(num, dziel):
    for i in range(1, num_1 + 1):
        if num % i == 0:
           dziel.append(i)


def szukanie_najw_wspól_dziel(dziel_1, dziel_2, dziel_3, nwd):
    for x in dziel_1:
        for y in dziel_2:
            for z in dziel_3:
                if x == y and y == z:
                    nwd = x
    return nwd


if __name__ == '__main__':
    dziel_1 = []
    dziel_2 = []
    dziel_3 = []

    nwd = 1

    num_1 = int(input("Podaj pierwszą liczbę: "))
    num_2 = int(input("Podaj drugą liczbę: "))
    num_3 = int(input("Podaj trzecią liczbę: "))

    dzielniki(num_1, dziel_1)
    dzielniki(num_2, dziel_2)
    dzielniki(num_3, dziel_3)

    result = szukanie_najw_wspól_dziel(dziel_1, dziel_2, dziel_3, nwd)

    print(f"Największym wspólnym dzielnikiem liczb {num_1}, {num_2}, {num_3} jest {result}")