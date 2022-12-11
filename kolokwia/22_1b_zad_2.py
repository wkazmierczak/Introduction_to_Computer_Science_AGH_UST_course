def square(T):
    l = len(T)
    for size in range(2, l):
        narozniki = [(0, size-1), (0, 0), (size-1, 0), (size-1, size-1)]
        for row in range(l-size+1):
            for column in range(l-size+1):
                iloczyn = 1
                for naroznik in narozniki:
                    a, b = naroznik
                    iloczyn *= T[row+a][column+b]
                if czy_tylko_dwa_rozne_czynniki(iloczyn):
                    return size
    return 0


def czy_tylko_dwa_rozne_czynniki(num):
    counter = 0
    i = 2
    while num != 1:
        if num % i == 0:
            counter += 1
            while num % i == 0:
                num //= i
        i += 1
    if counter == 2:
        return True
    else:
        return False


if __name__ == '__main__':
    T = [
        [2, 1, 1, 1, 1],
        [1, 1, 7, 1, 7],
        [1, 1, 1, 2, 1],
        [1, 1, 3, 1, 1],
        [1, 1, 1, 1, 5],
    ]
    print(square(T))

    #print(czy_tylko_dwa_rozne_czynniki(30))