def num_friends(num_1, num_2):
    num_digits_1 = [False for _ in range(10)]
    num_digits_2 = [False for _ in range(10)]
    while num_1 > 0:
        digit = num_1 % 10
        num_digits_1[digit] = True
        num_1 //= 10
    while num_2 > 0:
        digit = num_2 % 10
        num_digits_2[digit] = True
        num_2 //= 10
    return num_digits_1 == num_digits_2


def num_of_surr_only_by_friends(T):
    l = len(T)
    amount = l ** 2
    for x in range(l):
        for y in range(l):
            war = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < l and 0 <= y + j < l:
                        if not num_friends(T[x + i][y + j], T[x][y]):
                            war = False
            if not war:
                amount -= 1
    return amount


if __name__ == '__main__':
    T = [
        [13, 13, 13, 4, 4],
        [13, 13, 13, 4, 4],
        [13, 13, 13, 4, 5],
        [1, 2, 3, 100, 200],
        [1, 2, 3, 300, 5],
    ]
    print(num_of_surr_only_by_friends(T))
