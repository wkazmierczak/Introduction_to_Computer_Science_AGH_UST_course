i = 12
def czy_pierwsza(i):
    for y in range(2, i):
        if i % y == 0:
            return False
    return True

print(czy_pierwsza(31))