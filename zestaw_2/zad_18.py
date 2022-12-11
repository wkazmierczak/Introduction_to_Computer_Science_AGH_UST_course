def ciagi():
    n = int(input())
    x = 0
    a = 1
    b = 2
    if n == 0:
        print(b)
    else:
        print("Wrong")
        return False
    while n == x:
        n = int(input())
        a, b, x = a - b * x, b + 2 * a, a
        if n == x:
            print(b)
        else:
            print("Wrong")
            return False


if __name__ == '__main__':
    ciagi()