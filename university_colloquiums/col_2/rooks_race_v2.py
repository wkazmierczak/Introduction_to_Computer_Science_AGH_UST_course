from math import inf


def NWD(a, b):
    while b !=0:
        a, b = b, a%b
    return a


def race(T):
    l = len(T)-1
    left_speed = left_rook(T, 0, 0)
    right_speed = right_rook(T, 0, l)
    if left_speed > right_speed:
        return 1
    elif left_speed < right_speed:
        return 2
    else:
        return 0


def left_rook(T, w, k):
    l = len(T)
    if w == len(T) - 1 and k == len(T) - 1:
        return 0

    best_path = inf

    for new_k in range(k+1, l):
        if NWD(T[w][k], T[w][new_k]) == 1:
            best_path = min(left_rook(T, w, new_k) + 1, best_path)
    for new_w in range(w+1, l):
        if NWD(T[new_w][k], T[w][k]) == 1:
            best_path = min(left_rook(T, new_w, k) + 1, best_path)

    return best_path


def right_rook(T, w, k):
    l = len(T)
    if w == len(T) - 1 and k == 0:
        return 0

    best_path = inf

    for new_k in range(k-1, -1, -1):
        if NWD(T[w][k], T[w][new_k]) == 1:
            best_path = min(left_rook(T, w, new_k) + 1, best_path)
    for new_w in range(w + 1, l):
        if NWD(T[new_w][k], T[w][k]) == 1:
            best_path = min(left_rook(T, new_w, k) + 1, best_path)

    return best_path


if __name__ == '__main__':
    T = [[5, 3, 10, 20, 15],
         [2, 1, 3, 5, 7],
         [2, 1, 1, 5, 7],
         [2, 1, 3, 5, 7],
         [2, 1, 3, 5, 7]]
    print(race(T))
    # for i in range(4):
    #     print(i)
    # for i in range(4-1, -1, -1):
    #     print(i)