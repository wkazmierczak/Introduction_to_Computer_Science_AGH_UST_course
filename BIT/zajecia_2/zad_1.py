def NWD(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def NWW(a, b):
    return a * b // NWD(a, b)


if __name__ == '__main__':
    print(NWD(24, 20))
    print(NWW(24, 20))