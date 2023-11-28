# Zadanie 15. Problem 8 Hetmanów (treść oczywista)

def problem_8_hetman(T):
    counter = 0

    def rek(T, column=0):
        nonlocal counter
        if column == 8:
            print(T)
            counter += 1
            return

        for row in range(1, 9):
            if mozna(T, row, column):
                T[column] = row
                rek(T, column + 1)
            T[column] = 0

    rek(T)
    return counter


def mozna(T, row, column):
    b = column - 1
    if row in T:
        return False
    roz = row - column
    suma = row + column
    while b >= 0:
        if T[b] - b == roz or T[b] + b == suma:
            return False
        b -= 1
    return True


T = [0 for _ in range(8)]
print(problem_8_hetman(T))
