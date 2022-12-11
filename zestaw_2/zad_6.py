from math import sqrt


def smallest_diff(a):
    if a/sqrt(a) == a//sqrt(a):
        print(sqrt(a), "*", sqrt(a))
    for i in range(int(sqrt(a)), a+1):
        if a/i == a//i:
            print(i, "*", a//i)
            break


if __name__ == '__main__':
    smallest_diff(17)

