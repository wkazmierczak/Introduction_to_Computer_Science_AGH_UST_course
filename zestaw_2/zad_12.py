def twelve(num):
    suma = 0
    n = num
    while num > 0:
        x = num % 10
        num //= 10
        suma += x

    num = n

    while num > 0:
        x = num % 10
        num //= 10
        if suma == x:
            return True
    return False


if __name__ == '__main__':
    number = int(input("L: "))
    print(twelve(number))