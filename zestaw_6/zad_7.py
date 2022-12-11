# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
# Odważniki można umieszczać tylko na jednej szalce.

def odwazniki(T, m, i=0):
    l = len(T)
    if m == 0:
        return True
    if i == l:
        return False
    return odwazniki(T, m, i + 1) or odwazniki(T, m - T[i], i + 1)


if __name__ == '__main__':
    T = [2, 5, 10, 6, 3, 8]
    print(odwazniki(T, 4))
