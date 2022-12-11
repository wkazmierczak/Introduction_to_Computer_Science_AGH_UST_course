import random


def odd_checking(n):
    tab = [random.randint(1, 1000) for _ in range(n)]
    for i in tab:
        while i > 0:
            x = i % 10
            if x % 2 == 0:
                break
            i //= 10
        else:
            return True, tab
    return False, tab


if __name__ == '__main__':
    print(odd_checking(10))
