a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))
c = int(input("Trzecia liczba: "))
x = 0

while b != 0:
    x = b
    b = a % b
    a = x

print(a)
