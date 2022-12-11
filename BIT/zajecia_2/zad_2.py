from math import sqrt


def is_prime(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(num):
            if num % i == 0:
                return False
            i += 2
            if num % i == 0:
                return False
            i += 2

        return True


if __name__ == '__main__':
    print(is_prime(121))
