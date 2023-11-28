# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)

from math import sqrt

def zad_26(ones, zeros, num = "1"):
    if ones == 0 and zeros == 0 and is_not_prime(int(num)):
        #print(num)
        return 1
    if ones == 0:
        #print(num + zeros*'0')
        if is_not_prime(int(num + zeros*'0')):
            return 1
        else:
            return 0
    if zeros == 0:
        #print(num + ones*'1')
        if is_not_prime(int(num + ones*'1')):
            return 1
        else:
            return 0
    return zad_26(ones - 1, zeros, num + "1") + zad_26(ones, zeros - 1, num + "0")

def convert_num_to_dec(num):
    new_num = 0
    i = 0
    while num > 0:
        z = num % 2
        new_num = 2**(i)*z+ new_num
        num //=10
        i += 1
    return new_num

def is_not_prime(num):
    num = convert_num_to_dec(num)
    if num == 2 or num == 3:
        return False
    if num % 2 == 0 or num % 3 == 0 or num < 1:
        return True
    i = 5
    while i <= sqrt(num):
        if num % i == 0:
            return True
        i +=2
        if num % i == 0:
            return True
        i += 4
    return False

print(zad_26(1, 3))
#print(convert_num_to_dec(1111))
