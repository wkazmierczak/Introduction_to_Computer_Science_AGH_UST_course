# Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.

from math import sqrt


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
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


def convert_num_to_dec(num):
    new_num = 0
    i = 0
    while num > 0:
        x = num % 10
        new_num = new_num + (2**i)*x
        num //= 10
        i += 1
    return new_num


def ciagi(T, place=0, flag=False):
    l = len(T)
    if place >= l and flag:
        return True
    for i in range(2, 31):
        new_num = 0
        if place+i <= l:
            for x in T[place:place+i]:
                new_num = 10 * new_num + x
            if is_prime(convert_num_to_dec(new_num)):
                if ciagi(T, place+i, True):
                    return True
    return False


if __name__ == '__main__':
    T = [1, 1, 1, 0, 0, 0]
    print(ciagi(T))

