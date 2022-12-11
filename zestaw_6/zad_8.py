# Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

def odwazniki_na_obu_szalkach(T, m, i=0):
    l = len(T)
    if m == 0:
        return True
    if i == l:
        return False
    return odwazniki_na_obu_szalkach(T, m, i+1)\
        or odwazniki_na_obu_szalkach(T, m-T[i], i+1)\
        or odwazniki_na_obu_szalkach(T, m + T[i], i+1)


if __name__ == '__main__':
    T = [2, 7, 5, 3, 5, 8, 3, 9]
    print(odwazniki_na_obu_szalkach(T, 100))
