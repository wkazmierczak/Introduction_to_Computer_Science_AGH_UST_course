def decimal(a, b, n):
    print(a // b, end="")
    print(".", end="")
    for i in range(n):
        a = (a % b) * 10
        print(a // b, end="")


if __name__ == '__main__':
    decimal(5, 7, 100)
