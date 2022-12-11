from math import sqrt, log10


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num))+1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def liczby_pierwsze(num, curr=0, i=1, flag=False):
    leng = int(log10(num))+1
    if is_prime(curr) and curr > 9 and flag:
        print(curr)
    if i == leng+1:
        return
    else:
        return liczby_pierwsze(num, 10*curr+num//(10**(leng-i)) % 10, i+1, True)\
               or liczby_pierwsze(num, curr, i+1)


if __name__ == '__main__':
    liczby_pierwsze(1734)
