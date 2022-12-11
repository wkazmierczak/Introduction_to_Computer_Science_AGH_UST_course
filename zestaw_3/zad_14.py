from random import randint


def same_day_of_birth(n):
    tab = [-1 for _ in range(366)]
    counter = 0

    for i in range(100):
        for person in range(n):
            date = randint(0, 365)
            if tab[date] == i:
                counter += 1
                break
            else:
                tab[date] = i

    return counter/100


if __name__ == '__main__':
    print(same_day_of_birth(22))
