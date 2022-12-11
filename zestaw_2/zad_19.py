def periodic(a, b):
    digit_tab = [False for _ in range(b)]
    x = 0
    print(f"{a//b}.", end="")
    while True:
        x = a*10 // b
        a = a*10 % b
        if digit_tab[a]:
            break
        else:
            digit_tab[a] = True
        print(x, end="")


if __name__ == '__main__':
    periodic(1, 7)
    # a = int(input())
    # b = int(input())

