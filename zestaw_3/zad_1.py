def num_systems_counter(num, sys):

    arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    result = ""

    while num > 0:
        result = arr[num % sys] + result
        num //= sys
    return result


if __name__ == '__main__':
    print(num_systems_counter(45, 2))

