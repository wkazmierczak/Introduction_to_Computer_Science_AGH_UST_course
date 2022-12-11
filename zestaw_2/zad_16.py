def digits_sum(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def is_smith_number(n):

    divs_digits_sum = 0
    sum_digits_n = digits_sum(n)

    for div in range(2, n//2 + 1):
        if n % div == 0:
            div_digits_sum = digits_sum(div)
            while n % div == 0:
                divs_digits_sum += div_digits_sum
                n //= div
    return sum_digits_n == divs_digits_sum


if __name__ == '__main__':
    for x in range(1, 1000001):
        if is_smith_number(x):
            print(x)


