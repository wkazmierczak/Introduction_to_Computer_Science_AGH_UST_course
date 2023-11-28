def move(T):
    to_w = 0
    to_k = 0
    from_w = 0
    from_k = 0
    N = len(T)
    for x in range(N):
        counter_w = 0
        counter_k = 0
        for y in range(N):
            if T[x][y]:
                counter_w += 1
            if T[y][x]:
                counter_k += 1
        if counter_w == 0:
            to_w = x
        if counter_w > 1:
            from_w = x
        if counter_k == 0 and T[to_w][x]:
            to_k = x
        if counter_k > 1 and T[from_w][x]:
            from_k = x
    return (from_w, from_k), (to_w, to_k)


if __name__ == "__main__":
    T = True
    F = False
    T = [[F, F, F, F, F, F, T, F],
         [F, F, F, F, F, F, T, F],
         [F, F, F, F, F, T, F, F],
         [F, F, F, F, T, F, F, F],
         [F, F, F, T, T, F, F, F],
         [F, F, T, F, F, F, F, F],
         [F, T, F, F, F, F, F, F],
         [F, F, F, F, F, F, F, F]
         ]

    print(f"Trzeba przestawić wieżę z {move(T)[0]} na {move(T)[1]}")
