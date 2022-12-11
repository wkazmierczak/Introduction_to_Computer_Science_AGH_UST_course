def mozliwe_sumy(n, i, curr_sum=""):
    if n == 0:
        # if n == 1:
        #     curr_sum += "1"
        print(*curr_sum, sep=" + ")
    else:
        for x in range(1, min(i, n)+1):
            mozliwe_sumy(n-x, x, curr_sum + str(x))


if __name__ == '__main__':
    num = int(input("Podaj liczbę: "))
    mozliwe_sumy(num, num-1)
