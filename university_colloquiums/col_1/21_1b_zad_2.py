from math import sqrt
from math import log10


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num))+1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def rotate(n, n_len):
    x = n % 10
    n //= 10
    n = (10 ** (n_len-1))*x + n
    return n


def change_basis(num):
    n_len = int(log10(num))+1
    for basic in range(2, 17):
        for _ in range(n_len):
            num = rotate(num, n_len)
            new_num = 0
            i = 0
            iloczyn = 1
            curr_num = num
            print(curr_num)
            while curr_num > 0:
                x = curr_num % basic
                iloczyn *= x
                curr_num //= basic
                new_num = (10 ** i)*x + new_num
                i += 1
            print(new_num)
            if is_prime(iloczyn):
                return basic
    return None


if __name__ == '__main__':
    print(change_basis(122))

