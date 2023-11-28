def zad_2(x, y, n, i=0, A=0, B=0, C=0):
    if x == y:
        return i
    elif n == i:
        return n+1

    #return zad_2(x+3, y, n, i+1, 1, 0, 0) or zad_2(x*2, y, n, i+1 , 0, 1, 0) or zad_2(operacja_C(x), y, n, i+1, 0, 0, 1)

    if A== 0 and B==0 and C==0:
        res = min(zad_2(x+3, y, n, i+1, 1, 0, 0), zad_2(x*2, y, n, i+1 , 0, 1, 0), zad_2(operacja_C(x), y, n, i+1, 0, 0, 1))
        if res == n+1:
            return -1
        return res
    if A == 1:
        return min(zad_2(x*2, y, n, i+1, 0, 1, 0),zad_2(operacja_C(x), y, n, i+1, 0, 0, 1))
    if B == 1:
        return min(zad_2(x+3,y,n,i+1, 1, 0, 0) ,zad_2(operacja_C(x), y, n, i+1, 0, 0, 1))
    if C == 1:
        return min(zad_2(x+3, y, n, i+1, 1, 0, 0),zad_2(x*2, y, n, i+1, 0, 1, 0))


def operacja_C(num):
    c_num = num
    i = 0
    while c_num > 0:
        digit = c_num % 10 
        if digit % 2 == 1:
            num = num - 10**i
        c_num //= 10
        i += 1
    return num

if __name__ == "__main__":
    print(zad_2(23, 28, 10))
