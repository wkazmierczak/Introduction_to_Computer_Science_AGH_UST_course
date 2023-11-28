def kings_walk(T, w=0, k=0):
    leng = len(T)
    if w == leng-1 and k == leng-1:
        return T[w][k]

    if w < leng-1 and k < leng-1:
        return T[w][k] + min(kings_walk(T, w+1, k), kings_walk(T, w, k+1))
    elif w < leng-1:
        return T[w][k] + kings_walk(T, w+1, k)
    elif k < leng-1:
        return T[w][k] + kings_walk(T, w, k+1)


if __name__ == '__main__':
    T = [[4,3,4,5],
         [2,3,4,5],
         [2,3,1,5],
         [1,1,1,1]]
    print(kings_walk(T))