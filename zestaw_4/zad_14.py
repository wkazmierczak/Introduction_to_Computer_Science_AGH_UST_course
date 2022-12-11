def czy_zgodne(a, b):
    counter_a = 0
    counter_b = 0
    while a > 0:
        x = a % 2
        if x == 1:
            counter_a += 1
        a //= 2

    while b > 0:
        x = b % 2
        if x == 1:
            counter_b += 1
        b //= 2

    return counter_a == counter_b


def tab_moving(T1, T2):
    len_b = len(T1)
    len_s = len(T2)
    for x in range(len_b-len_s+1):
        for y in range(len_b-len_s+1):
            counter = 0
            for a in range(len_s):
                for b in range(len_s):
                    if czy_zgodne(T1[x+a][y+b], T2[a][b]):
                        counter += 1
            if counter/(len_s**2) > 0.33:
                return True
    return False


if __name__ == '__main__':
    T1 = [
        [1, 1, 1, 1, 1],
        [1, 2, 1, 1, 7],
        [1000, 1000, 1000, 1000, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]

    T2 = [[7, 7],
          [7, 7]
    ]
    print(tab_moving(T1, T2))