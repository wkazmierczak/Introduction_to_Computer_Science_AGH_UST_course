def area_counter(n, k):
    # y = 1 / x
    area = 0
    for i in range(1, n+1):
        area += (k-1)/n * 1/(1+i*(k-1)/n)
    return area


if __name__ == '__main__':
    print(area_counter(100, 5))

