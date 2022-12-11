def problem_skoczka_szachowego(T, x, y, n=1):
    l = len(T)
    T[x][y] = n
    if n == l**2:
        return True

    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for move in moves:
        a, b = move
        if 0 <= x+a < l and 0 <= y+b < l and T[x+a][y+b] == 0:
            if problem_skoczka_szachowego(T, x + a, y + b, n + 1):
                return True

    T[x][y] = 0
    return False


if __name__ == '__main__':
    T = [[0 for _ in range(5)] for _ in range(5)]
    problem_skoczka_szachowego(T, 0, 0)
    for row in T:
        print(row)
