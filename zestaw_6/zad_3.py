def kings_walk(t, k, row=0):
    l = len(t)
    if row == 7:
        return t[row][k]
    elif 0 <= k+1 < l and 0 <= k-1 < l:
        return t[row][k] + min(kings_walk(t, k, row+1), kings_walk(t, k+1, row+1), kings_walk(t, k-1, row+1))
    elif 0 <= k+1 < l:
        return t[row][k] + min(kings_walk(t, k, row+1), kings_walk(t, k+1, row+1))
    elif 0 <= k-1 < l:
        return t[row][k] + min(kings_walk(t, k, row + 1), kings_walk(t, k - 1, row + 1))


if __name__ == '__main__':
    t = [[7, 3, 6, 4, 1, 4, 8, 5],
         [7, 3, 6, 1, 5, 1, 8, 5],
         [7, 3, 6, 4, 1, 1, 8, 5],
         [7, 3, 6, 1, 5, 4, 1, 5],
         [7, 3, 1, 4, 5, 4, 8, 1],
         [7, 1, 6, 4, 5, 4, 8, 1],
         [1, 3, 6, 4, 5, 4, 8, 1],
         [1, 3, 6, 4, 5, 4, 8, 1]]
    print(kings_walk(t, 4))
