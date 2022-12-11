from math import log10


def czytrzyjedynki(bin):
    counter = 0
    while bin > 0:
        if bin % 2 == 1:
            counter += 1
        bin //= 2
    if counter == 3:
        return True
    else:
        return False


def scalanie(num1, num2):
    leng1 = int(log10(num1)) + 1
    leng2 = int(log10(num2)) + 1
    N = leng1 + leng2
    for mask in range(7, 2**N):
        if czytrzyjedynki(mask):
            n1 =num1
            n2 = num2
            i = 0
            result = 0
            while mask > 0 or n2 > 0:
                if mask % 2 == 1:
                    d = n1 % 10
                    n1 //= 10
                else:
                    d = n2 % 10
                    n2 //= 10
                mask //= 2
                result = d*(10**i) + result
                i += 1
            print(result)


def zadanie(tekst, klucz):
    dl = len(tekst)

    for i in range(dl//klucz+1):
        for j in range(klucz):
            if i*klucz+j < dl:
                print(tekst[i*klucz+j], end="")
        print("")

def tab():

    tab = [(0,i) for i in range(10)]
    for start in tab:
        x, y = start
        print(y)

if __name__ == '__main__':
    print(tab())


