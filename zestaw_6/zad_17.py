from math import log10, sqrt


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False
    i = 5
    while i < int(sqrt(num)) + 1:
        if num % i == 0:
            return False
        i += 2
        if num % i == 0:
            return False
        i += 4
    return True


def creating_third_num(num1, num2, new_num=''):
    if not num1 and not num2:
        if is_prime(int(new_num)):
            print(new_num)
            return True

    return creating_third_num(num1[1:], num2, new_num+num1[0]) or creating_third_num(num1, num2[1:], new_num + num2[0])


def creating_third_num_v2(num1, num2, new_num=0):
    len_1 = log10(num1)+1
    len_2 = log10(num2)+1
    if num1 == 0 and num2 == 0:
        if is_prime(new_num):
            print(new_num)
            return True
    return creating_third_num_v2(num1 % 10**(len_1-1), num2, 10*new_num+(num1//10**(len_1-1))%10) \
            or creating_third_num_v2(num1, num2 % 10**(len_2-1), 10*new_num+(num2//10**(len_2-1))%10)


if __name__ == '__main__':
    num_f = input()
    num_s = input()
    #creating_third_num_v2(num_f, num_s)
    creating_third_num(num_f, num_s)
