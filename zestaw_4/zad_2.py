def even_in_every_row(tab):
    a = False
    for tab_1 in tab:
        for num in tab_1:
            a = True
            while num > 0:
                if num % 2 == 0:
                    a = False
                num //= 10
            if a:
                break
    return a


if __name__ == '__main__':
    tab = [[12, 34], [15, 43, 6], [17, 2, 43]]
    print(even_in_every_row(tab))