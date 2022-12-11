def skoczki(T, n):
    l = len(T)
    counter = 0
    for x in range(l):
        for y in range(l):
            for a in range(-2, 3, 2):
                for b in range(-1, 2, 2):
                    try:
                        if T[x][y] * T[x+a][y+b] == n or T[x][y] * T[x+b][y+a] == n:
                            counter += 1
                    except:
                        continue
    return counter


if __name__ == '__main__':
    T = [[1, 2, 3, 4, 5, 6, 7, 8],
         [2, 4, 3, 5, 6, 4, 2, 1],
         [1, 2, 3, 4, 5, 6, 7, 8],
         [2, 4, 3, 5, 6, 4, 2, 1],
         [1, 2, 3, 4, 5, 6, 7, 8],
         [2, 4, 3, 5, 6, 4, 2, 1],
         [1, 2, 3, 4, 5, 6, 7, 8],
         [2, 4, 3, 5, 6, 4, 2, 1]
         ]

    print(skoczki(T, 6))