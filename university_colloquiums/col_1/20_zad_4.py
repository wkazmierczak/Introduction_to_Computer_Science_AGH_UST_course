from math import log10, log2, sqrt


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def NWW(a, b):
    return a * b // NWD(a,b)


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num)+1):
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True

# def divide(num):
#     N = int(log10(num))
#     for mask in range(1, 2**N):



if __name__ == '__main__':
    #print(divide(1613))
    #print(convert_to_bin(2125, 2))
    print(is_prime(7))
    #print(NWD(21, 21))
    #print(int(log10(12833)))
    print([2]+[3,4])