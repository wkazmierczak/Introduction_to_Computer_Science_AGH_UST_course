def spirala(n):
    tab = [[0 for _ in range(n)] for _ in range(n)]
    y = 0
    x = 0
    num = 0
    for i in range(n//2+1):
        while tab[x][y] == 0:
            num += 1
            tab[x][y] = num
            if y == n-1:
                break
            if tab[x][y+1] == 0:
                y += 1
        x += 1

        while tab[x][y] == 0:
            num += 1
            tab[x][y] = num
            if x == n-1:
                break
            if tab[x+1][y] == 0:
                x += 1
        y -= 1

        while tab[x][y] == 0:
            num += 1
            tab[x][y] = num
            if y == n-1 or y == 0:
                break
            if tab[x][y - 1] == 0:
                y -= 1
        x -= 1

        while tab[x][y] == 0:
            num += 1
            tab[x][y] = num
            if x == n-1 or x == 0:
                break
            if tab[x - 1][y] == 0:
                x -= 1
        y += 1

    for tab_1 in tab:
        print(tab_1)
    #print(tab)


if __name__ == '__main__':
    spirala(10)