def check_condition(n):
    suma = 0
    num_2 = n
    for i in range(len(str(n))):
        x = num_2 % 10
        num_2 //= 10
        suma += x**(len(str(n)))
    return suma == n


def nums_iteration():
    for n in range(1, 10000001):
        if check_condition(n):
            print(n, check_condition(n))


if __name__ == '__main__':
    nums_iteration()


