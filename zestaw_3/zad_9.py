def najdluzszy_podciag_rosnacy(tab):
    i = 0
    longest = 1
    counter = 1
    while i < (len(tab) - 1):
        if tab[i] < tab[i + 1]:
            #while i < (len(tab) - 1) and tab[i] < tab[i + 1]:
            counter += 1
        else:
            if counter > longest:
                longest = counter
            counter = 1
        i += 1

    if counter > longest:
        longest = counter
        
    return longest


if __name__ == '__main__':
    tab = [1, 2, 1, 4, 5, 6, 7]
    print(najdluzszy_podciag_rosnacy(tab))