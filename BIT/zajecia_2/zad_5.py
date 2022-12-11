def binary_search(n, arr):
    if len(arr) == 1:
        return arr[0] == n

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == n:
            return True
        elif arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


def NWD(a, b):
    while b != 0:
        a, b = b, b % a
    return a


def NWW(a, b):
    return a * b // NWD(a,b)


if __name__ == '__main__':
    #print(binary_search(34, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(NWD(45, 60))
    print(NWW(45, 60))