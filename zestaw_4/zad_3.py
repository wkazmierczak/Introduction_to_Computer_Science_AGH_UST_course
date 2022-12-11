def at_least_one_digit_even(tab):
    for tab_1 in tab:
        for num in tab_1:
            a = True
            while num > 0:
                digit = num % 10
                num //= 10
                if digit % 2 == 0:
                    a = False
            if a:
                return False
    return True


if __name__ == '__main__':
    tab = [[21, 34], [2, 4, 6], [12, 2, 34]]
    print(at_least_one_digit_even(tab))
