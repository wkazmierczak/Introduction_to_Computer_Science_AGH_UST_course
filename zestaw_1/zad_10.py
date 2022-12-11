def if_perfect(suma, num):
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            suma += i
    if suma == num:
        print("Twoja liczba jest liczbą doskonałą")
    else:
        print("Twoja liczba nie jest liczbą doskonałą")


if __name__ == '__main__':
    suma = 0
    num = int(input("Podaj liczbę: "))
    if_perfect(suma, num)
