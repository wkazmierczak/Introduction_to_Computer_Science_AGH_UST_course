def najdluzszy_podciag_geometryczny(tab):
    counter = 2
    i = 0
    longest = 2
    while i < len(tab) - 2:
        if tab[i + 1] / tab[i] == tab[i+2]/ tab[i+1]:
            counter += 1
        else:
            counter = 2
        if counter > longest:
            longest = counter
        i += 1
    return longest


if __name__ == '__main__':
    tab = [1, 2, 4, 8, 3, 48, 24, 12, 6, 3, 2]
    print(najdluzszy_podciag_geometryczny(tab))