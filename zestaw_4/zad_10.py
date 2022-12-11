def zero_in_every_row_and_column(T):
    return zero_in_every_row(T) and zero_in_every_column(T)


def zero_in_every_row(T):
    n = len(T)
    x = 0
    while x < n:
        y = 0
        while y < n:
            if T[x][y] == 0:
                x += 1
                break
            y += 1
        else:
            return False
    return True


def zero_in_every_column(T):
    n = len(T)
    x = 0
    while x < n:
        y = 0
        while y < n:
            if T[y][x] == 0:
                x += 1
                break
            y += 1
        else:
            return False
    return True

    # while y < n:
    #     while x < n:
    #         if T[x][y] == 0:
    #             x += 1
    #             break
    #         y += 1
    #     else:
    #         b = False


if __name__ == '__main__':
    T = [
        [1, 0, 0, 0, 0],
        [2, 0, 4, 100, 6],
        [0, 0, 100, 5, 6],
        [3, 0, 4, 5, 6],
        [2, 0, 4, 5, 6]
    ]

    print(zero_in_every_row_and_column(T))