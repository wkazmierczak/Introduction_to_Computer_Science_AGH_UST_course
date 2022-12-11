# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)

def zad_26(ones, zeros, num = "1"):
    if ones == 0 and zeros == 0:
        print(num)
        return
    if ones == 0:
        print(num + zeros*'0')
        return
    if zeros == 0:
        print(num + ones*'1')
        return
    return zad_26(ones - 1, zeros, num + "1") or zad_26(ones, zeros - 1, num + "0")

zad_26(1, 3)
