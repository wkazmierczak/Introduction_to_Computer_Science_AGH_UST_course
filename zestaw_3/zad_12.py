import random


def fun(n):
    tab = [random.randrange(1, 100, 2) for _ in range(n)]
    #tab = [1, 2, 3, 4, 9, 8, 7, 6, 5, 4, 3]
    i = 0
    longest_plus = 2
    longest_minus = 2
    counter_plus = 2
    counter_minus = 2

    while i < len(tab) - 2:
        if tab[i + 1] - tab[i] == tab[i+2] - tab[i+1]:
            if tab[i + 1] - tab[i] > 0:
                counter_plus += 1
            elif tab[i + 1] - tab[i] < 0:
                counter_minus += 1
        else:
            counter_minus = 2
            counter_plus = 2
        if longest_minus < counter_minus:
            longest_minus = counter_minus
        elif longest_plus < counter_plus:
            longest_plus = counter_plus
        i += 1

    return longest_plus - longest_minus


if __name__ == '__main__':
    print(fun(260))
