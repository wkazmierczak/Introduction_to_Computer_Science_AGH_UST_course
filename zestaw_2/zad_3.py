def if_palindrom(num):
    i = 2
    num_2 = 0
    cur_num = num
    while cur_num > 0:
        x = cur_num % i
        #print(x)
        cur_num //= i
        #print(cur_num)
        num_2 *= i
        #print(num_2)
        num_2 += x
        #print(num_2)

    return num == num_2


if __name__ == '__main__':
    print(if_palindrom(17))
