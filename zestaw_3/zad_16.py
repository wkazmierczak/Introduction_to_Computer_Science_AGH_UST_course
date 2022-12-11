def biggest_lowest(tab):
    lowest = tab[0]
    biggest = tab[0]
    for element in tab:
        if element > biggest:
            biggest = element
        if element < lowest:
            lowest = element
    if tab.count(lowest) == tab.count(biggest) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    tab = [1, 4, 5, 6, 4, 22, 5, 22]
    print(tab)
    print(biggest_lowest(tab))