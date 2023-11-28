from math import inf


def first_line(T, w=0):
    for k in range(len(T)):
        if not T[0][k]:
            if skoczek_ze_zliczniem(T, k, w) == inf:
                return False
            return skoczek_ze_zliczniem(T, k)
    return False


def skoczek_ze_zliczniem(T, k, w=0, cnt=0):
    l = len(T)
    if k < 0 or k >= l or w >= l or T[w][k]:
        return inf

    if w == len(T)-1:
        return cnt

    return min(skoczek_ze_zliczniem(T, k+1, w+2, cnt + 1),
               skoczek_ze_zliczniem(T, k-1, w+2, cnt + 1),
               skoczek_ze_zliczniem(T, k-2, w+1, cnt + 1),
               skoczek_ze_zliczniem(T, k+2, w+1, cnt + 1))


def skoczek(T, k, w=0):
    l = len(T)
    moves = [(1, 2), (1, -2), (2, 1), (2, -1)]

    if w == len(T)-1:
        return True

    for a, b in moves:
        if w+a < l and 0 <= k+b < l and not T[w+a][k+b]:
            if skoczek(T, k+b, w+a):
                return True
    return False


if __name__ == '__main__':
    t = True
    f = False
    T = [[t, f, t, t],
         [f, t, t, f],
         [t, f, t, t],
         [f, t, t, f]]
    print(first_line(T))
