def hanoi(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    return 2*hanoi(n-1) + 1


if __name__ == '__main__':
    print(hanoi(5))

# 2  3
# 3  7
# 4  15
# 5  31
