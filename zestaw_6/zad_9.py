# Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.

def odwazniki_na_obu_szalkach(T, m, odwazniki="", i=0):
    l = len(T)
    if m == 0:
        return True
    if i == l:
        return False
    return odwazniki_na_obu_szalkach(T, m, odwazniki, i+1)\
        or odwazniki_na_obu_szalkach(T, m - T[i], odwazniki+str(T[i]), i+1)


if __name__ == '__main__':
    T = [2, 7, 5, 3, 5, 8, 3, 10]
    print(odwazniki_na_obu_szalkach(T, 9))