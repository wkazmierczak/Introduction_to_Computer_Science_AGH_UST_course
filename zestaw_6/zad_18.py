from math import log10


def kings_walk(T, w=0, k=0):
    l = len(T)
    x = T[7][7]
    leng_x = int(log10(x))+1
    x_first_digit = (x//10**(leng_x-1)) % 10

    if w == 7 and k == 7:
        return True
    moves = [(1, 0), (1, 1), (0, 1)]
    for move in moves:
        a, b = move
        if w+a < 8 and k+b < 8:
            if x_first_digit > T[w+a][k+b] % 10:
                return kings_walk(T, w+a, k+b)
        if w+1 < 8:
            if x_first_digit > T[w+1][k] % 10:
                return kings_walk(T, w+1, k)
        if k+1 < 8:
            if x_first_digit > T[w][k+1] % 10:
                return kings_walk(T, w, k+1)

    return False


if __name__ == '__main__':
    T = [[1, 2, 3, 4, 5, 6, 7, 8],
         [2, 1, 3, 5, 6, 6, 7, 8],
         [2, 2, 1, 5, 6, 4, 2, 1],
         [1, 2, 3, 2, 5, 4, 2, 1],
         [1, 2, 2, 4, 1, 6, 7, 8],
         [2, 4, 3, 2, 6, 1, 2, 1],
         [1, 2, 3, 4, 2, 6, 1, 8],
         [2, 4, 3, 5, 6, 2, 2, 23834781]
         ]

    print(kings_walk(T))
