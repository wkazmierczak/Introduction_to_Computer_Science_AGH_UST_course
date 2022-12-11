def counting_row_sum(T, row):
    row_sum = 0
    for elem in T[row]:
        row_sum += elem
    return row_sum


def counting_column_sum(T, column):
    l = len(T)
    column_sum = 0
    for x in range(l):
        column_sum += T[x][column]
    return column_sum


def best_rooks_setting(T):
    l = len(T)
    biggest_sum = 0
    for x in range(l):
        for y in range(l):
            for a in range(l):
                for b in range(l):
                    if x == a and y == b:
                        continue
                    if a == x:
                        total_sum = counting_row_sum(T, x) + counting_column_sum(T, y) \
                                     + counting_column_sum(T, b) - T[x][y] - T[a][b]
                    elif b == y:
                        total_sum = counting_row_sum(T, x) + counting_column_sum(T, y) \
                                    + counting_row_sum(T, a) - T[x][y] - T[a][b]
                    else:
                        total_sum = counting_row_sum(T, x) + counting_column_sum(T, y) \
                                    + counting_row_sum(T, a) + counting_column_sum(T, b) \
                                    - 2 * T[x][y] - 2 * T[a][b] - T[a][y] - T[x][b]
                    if total_sum > biggest_sum:
                        row_1 = x
                        column_1 = y
                        row_2 = a
                        column_2 = b
                        biggest_sum = total_sum
    return row_1, column_1, row_2, column_2


if __name__ == '__main__':
    T = [
        [1, 1, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1000, 1000, 1000, 1000, 1000],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print(best_rooks_setting(T))
