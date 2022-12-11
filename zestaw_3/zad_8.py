from math import sqrt


def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    else:
        i = 5
        while i < int(sqrt(num)+1):
            if num % i == 0:
                return False
            i += 2
            if num % i == 0:
                return False
            i += 4
        return True


def skakanie_po_indeksach(t, k):
    divs_list = []
    if k == int(len(arr) - 1):
        return []
    if k > int(len(arr) - 1):
        return []
    for i in range(1, int(t[k]) + 1):
        if t[k] % i == 0:
            if i not in divs_list and is_prime(i):
                divs_list.append(i)
    return divs_list


def checking(arr, k):
    for z in skakanie_po_indeksach(arr, k):
        print(z)
        k += z
        print(skakanie_po_indeksach(arr, k))
        checking(arr, k)


if __name__ == '__main__':
    k = 0
    arr = [642, 2, 34, 564, 4, 4, 34]
    x = skakanie_po_indeksach(arr, k)

    print(checking(arr, k))

    #print(checking(arr, k, x))

    #print(skakanie_po_indeksach([2564, 5, 6, 4, 7, 3], 0))
    #print(skakanie_po_indeksach([3423,434, 35959, 4], 0))
    #print(skakanie_po_indeksach(arr, k))

    # for y in x:
    #     print(y)
    #     k += y
    #     print(skakanie_po_indeksach(arr, k))
    #     for z in skakanie_po_indeksach(arr, k):
    #         print(z)
    #         k += z
    #         print(skakanie_po_indeksach(arr, k))


