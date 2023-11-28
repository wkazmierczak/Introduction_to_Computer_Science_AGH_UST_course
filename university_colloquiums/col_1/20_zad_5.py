def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def trojki(T):
    N = len(T)
    counter = 0
    for i in range(N):
        for x in range(1, 3):
            for y in range(1, 3):
                if x + i + y >= N or i+x >= N or i+y >= N:
                    continue
                if NWD(T[i], T[i+x+y]) == 1 and NWD(T[i+x], T[i+x+y]) == 1 and NWD(T[i], T[i+x]) == 1:
                    counter += 1
    return counter


if __name__ == '__main__':
    print(trojki([2,3,4,5,6,8,7]))