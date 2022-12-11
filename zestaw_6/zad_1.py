from math import sqrt, log10


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num)) + 1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def new_num(num, flag=False):
    n = int(log10(num)) + 1
    if n < 2:
        return 1
    if is_prime(num) and flag:
        print(num)

    new_num(num // 10, flag=True)
    new_num(num % 10**(n-1), flag=True)


def rek(n, result=0, pos=0, b=False):
    if n == 0:
        if result > 9 and b and is_prime(result):
            print(result)
        return
    rek(n // 10, result, pos, True)
    rek(n // 10, result + ((n % 10) * 10 ** pos), pos + 1, b)


if __name__ == '__main__':
    new_num(739871)
    print("\n")
    rek(739871)

