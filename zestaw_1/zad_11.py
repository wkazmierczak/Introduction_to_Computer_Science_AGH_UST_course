def sumowanie(num, suma):
    for i in range(1, (num//2)+1):
        if num % i == 0:
            suma += i
    return suma


def czy_zaprzyjaznione(num_1, num_2, suma_1, suma_2):
    if suma_1 == num_2 and suma_2 == num_1 and num_1 != num_2:
        print(f"{num_1} oraz {num_2} są liczbami zaprzyjaźnionymi")


if __name__ == '__main__':
    for num_1 in range(1, 1000001):
        suma_1 = 0
        suma_2 = 0
        #sumowanie(num_1, suma_1)
        num_2 = sumowanie(num_1, suma_1)
        suma_1 = sumowanie(num_1, suma_1)
        suma_2 = sumowanie(num_2, suma_2)
        czy_zaprzyjaznione(num_1, num_2, suma_1, suma_2)

