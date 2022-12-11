
def spirala(size):
    kierunki = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    num = 1
    x, y = 0, 0

    tab = [[0 for _ in range(size)] for _ in range(size)]

    while size - 1 > 0:
        for kierunek in kierunki:
            a, b = kierunek
            for i in range(size - 1):
                tab[y][x] = num
                x, y = x + a, y + b
                num += 1
        x, y = x+1, y+1
        size -= 2

    if tab[y][x] == 0:
        tab[y][x] = num
    for row in tab:
        print(row)


if __name__ == '__main__':
    spirala(6)
