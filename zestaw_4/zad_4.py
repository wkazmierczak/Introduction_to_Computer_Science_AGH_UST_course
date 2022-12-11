def najwiekszy_iloraz_suma_rzedu_suma_kolumny(tab):
    suma_row = 0
    biggest_column = 0
    column = 0
    row = 0

    for num in tab[0]:
        suma_row += num
    smallest_row = suma_row

    # for row in tab:
    #     suma_row = 0
    #     for num in row:
    #         suma_row += num
    #     if suma_row < smallest_row:
    #         smallest_row = suma_row
    #         row_1 = row

    for x in range(len(tab)):
        suma_column = 0
        suma_row = 0
        for y in range(len(tab)):
            suma_column += tab[y][x]
            suma_row += tab[x][y]
        if suma_row < smallest_row and suma_row != 0:
            smallest_row = suma_row
            row = x
        if suma_column > biggest_column:
            biggest_column = suma_column
            column = x

    return column, row


if __name__ == '__main__':
    tab = [
        [1, 1, 1, 1, 100],
        [2, 3, 4, 100, 6],
        [2, 3, 100, 5, 6],
        [3, 300, 4, 5, 6],
        [2, 3, 4, 5, 6],

    ]

    print(najwiekszy_iloraz_suma_rzedu_suma_kolumny(tab))
