def how_many_palindroms(array):
    num = 0
    for i in array:
        if i != "" and i == i[::-1]:
            num += 1
    return num


if __name__ == '__main__':
    arr = ["" for _ in range(10)]
    arr[3] = "12321"
    print(arr)
    print(how_many_palindroms(arr))