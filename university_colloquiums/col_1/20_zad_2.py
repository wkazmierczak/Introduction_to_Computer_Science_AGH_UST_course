def min_row(T):
    pos_min = 0
    N = len(T)
    for row in range(1, N):
        column = 0
        while T[row][column] == T[pos_min][column]:
            column += 1
        if T[row][column] == 0:
            pos_min = row
    return pos_min


def max_row(T):
    pos_max = 0
    N = len(T)
    for row in range(1, N):
        column = 0
        while T[row][column] == T[pos_max][column]:
            column += 1
        if T[row][column] == 1:
            pos_max = row
    return pos_max


def distance(T):
    pos_max = max_row(T)
    pos_min = min_row(T)
    return abs(pos_max-pos_min)


if __name__ == '__main__':
    T = [
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1],
    ]
    print(distance(T))