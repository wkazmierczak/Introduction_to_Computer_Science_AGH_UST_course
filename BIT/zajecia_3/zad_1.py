def zad_1():
    arr = [i **2 if i % 10 == 0 else i for i in range(1,51)]
    return arr


def zad_2():
    arr = [n for n in range(1,101) if is_prime(n)]
    return arr


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    else:
        i = 5
        while i <= n**0.5:
            if n % i == 0:
                return False
            i += 2
            if n % i == 0:
                return False
            i += 4
        return True


def zad_6():
    arr = [(892, "ajkshfdjash"), (4837, 'skdjkk')]
    print(sorted(arr, key = lambda x: x[1]))


def zad_8():
    def sieve_of_eratosthenes(num):
        prime = [True for i in range(num)]
        # boolean array
        p = 2
        while (p * p < num):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Updating all multiples of p
                for i in range(p * p, num + 1, p):
                    prime[j] = False

        # Print all prime numbers
        for p in range(2, num + 1):
            if prime[p]:
                print(p)

    # Driver code
    if __name__ == '__main__':
        num = 50
        sieve_of_eratosthenes(num)


if __name__ == '__main__':
    #print(zad_1())
    #print(zad_2())
    #zad_6()