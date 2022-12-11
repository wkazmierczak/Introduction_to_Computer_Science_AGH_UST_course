def najdluzszy_podciag_arytmetyczny(tab):
    i = 0
    counter = 2
    longest = 2

    while i < len(tab) - 2:
        if tab[i + 1] - tab[i] == tab[i + 2] - tab[i + 1]:
            counter += 1
        else:
            counter = 2

        if counter > longest:
            longest = counter
            
        i += 1

    return longest


if __name__ == '__main__':
    tab = [1, 2, 4, 5, 3, 5, 7, 5, 6, 3, 2]
    print(najdluzszy_podciag_arytmetyczny(tab))

