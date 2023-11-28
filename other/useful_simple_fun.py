from math import sqrt


def pierwsza(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num <= 1:
        return False
    i = 5
    while i < int(sqrt(num))+1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def NWW(a, b):
    return int(a*b/NWD(a,b))


if __name__ == '__main__':
    print(pierwsza(5))
    #print(NWD(9, 3))
    #print(NWW(9, 4))