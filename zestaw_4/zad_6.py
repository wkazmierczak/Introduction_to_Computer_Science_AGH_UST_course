from math import inf


def finding_lowest(T1, indxs):
    result = 0
    for i in range(1, len(T1)):
        if T1[i][indxs[i]] < T1[result][indxs[result]]:
            result = i
    return result


def zad_6(T1):
    l = len(T1)
    T2 = [0 for _ in range(l**2)]
    i = 0
    indxs = [0 for _ in range(l)]
    prev = -1
    T_i =0
    while i < l**2:
        element = finding_lowest(T1, indxs)
        if T1[element][indxs[element]] != prev:
            prev = T2[T_i] = T1[element][indxs[element]]
            T_i += 1
        if indxs[element] == l-1:
            T1[element][indxs[element]] = inf
        else:
            indxs[element] += 1
        i += 1
    return T2


if __name__ == '__main__':

    T1 = [
        [1, 2, 5, 6],
        [3, 4, 9, 10],
        [7, 11, 13, 15],
        [8, 12, 14, 16]
    ]
    print(zad_6(T1))

