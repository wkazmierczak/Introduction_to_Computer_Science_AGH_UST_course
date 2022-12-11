import random


def najdluzszy_ciag_z_rewersem():
    tab = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
    #tab = [1, 2, 3, 3, 2, 1]
    #[random.randint(100, 999) for _ in range(n)]
    r_tab = tab[::-1]
    i = 0
    counter = 1
    longest = 1
    while i < len(tab):
        if tab[i] in r_tab:
            x = r_tab.index(tab[i])
            curr_i = i
            while tab[curr_i] == r_tab[x] and curr_i < len(tab) - 1 and x < len(r_tab) - 1:
                counter += 1
                curr_i += 1
                x += 1
                if curr_i == len(tab) - 1:
                    longest = counter
                    return longest
        if counter > longest:
            longest = counter
            counter = 0
        i += 1
    return longest


if __name__ == '__main__':
    print(najdluzszy_ciag_z_rewersem())
