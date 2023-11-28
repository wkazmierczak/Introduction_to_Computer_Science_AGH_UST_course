# Na szachownicy NxN ułożono pewną liczbę pionków których położenie opisusje tablica L.
# Z lewego górnego rogu startuje wieża, która chce dojść do prawego dolnego rogu szachownicy.
# wieża porusza sie tylko w prawo i w dół. Wieża nie może zbić pionka.
# Napisz funkcje rook która zwróci minimalną liczbę ruchów potrzebnych wieży, aby dotrzeć do celu.
# Jeżeli jest to niemożliwe zwróć None.

from math import inf


def rook(N, L):
    min_path = inf

    def rek(N, L, w=0, k=0, cnt=0):
        nonlocal min_path
        if w >= N or k >= N:
            return
        if w == N - 1 and k == N - 1:
            min_path = min(min_path, cnt)
            return
        for new_w in range(w + 1, N):
            if (new_w, k) in L:
                break
            rek(N, L, new_w, k, cnt + 1)

        for new_k in range(k + 1, N):
            if (w, new_k) in L:
                break
            rek(N, L, w, new_k, cnt + 1)
    rek(N, L)
    if min_path == inf:
        return None
    return min_path


if __name__ == "__main__":
    N = 8
    L = [(0,1), (1,0), (1,2), (2,5), (4,7), (3, 8)]
    print(rook(8, L))
