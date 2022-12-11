from math import sqrt


def check(num):
    for n in range(1, int(sqrt(num)) + 1):
        if num % (n**2 + n + 1) == 0:
            print(n)
            return True
    return False


if __name__ == '__main__':
    print(check(22))
