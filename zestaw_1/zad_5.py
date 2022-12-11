def finding_sqrt(a, b, area):
    a = (a + b) / 2
    b = area/a
    return a


if __name__ == '__main__':
    a = 1
    area = int(input("Wprowadź liczbę: "))
    b = area
    while round(a, 5) != round(b, 5):
        a = (a + b) / 2
        b = area / a
    print(round(a, 2))

