def biggest_surr_sum(T):
    l = len(T)
    row = 0
    column = 0
    biggest_suma = 0
    for x in range(l):
        for y in range(l):
            current_sum = surr_sum(T, x, y)
            if biggest_suma < current_sum:
                row = x
                column = y
                biggest_suma = current_sum

    return row, column


def surr_sum(T, x, y):
    l = len(T)
    suma = - T[x][y]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if l > x+i >= 0 and l > y + j >= 0:
                suma += T[x+i][y+j]

    return suma


if __name__ == '__main__':
    T = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 100, 200],
        [1, 2, 3, 300, 5],
    ]

    print(biggest_surr_sum(T))