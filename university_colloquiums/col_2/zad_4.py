# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
# pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
# liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
# 23 i 47, natomiast divide(2255)=False

from math import sqrt, log10

def is_prime(num):
    if num ==2 or num ==3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 0:
        return False
    i = 5
    while i < sqrt(num)+1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def divide(num, parts=0):
    if num == 0:
        return is_prime(parts)

    l = int(log10(num)) + 1

    for i in range(l-1, -1, -1):
        curr_num = num // 10**i
        if is_prime(curr_num):
            if divide(num % 10**i, parts+1):
                return True
    return False

    #if is_prime(curr_num):


if __name__ == "__main__":
    print(divide(22222))
    #print(is_prime(31))
