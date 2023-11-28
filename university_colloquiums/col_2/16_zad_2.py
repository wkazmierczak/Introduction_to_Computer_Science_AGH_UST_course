# def dec_to_bin(num):
#     i = 0
#     new_num = 0
#     while num > 0:
#         x = num % 2
#         new_num = x*10**i + new_num
#         num //= 2
#         i += 1
#     return new_num

def dec_to_bin(num):
    cnt = 0
    while num > 0:
        if num % 2 == 1:
            cnt += 1
        num //= 2
    return cnt


def zad_2(T, sum_1=0, sum_2=0, sum_3=0, i=0):
    if sum_1 == sum_2 and sum_3 == sum_1 and sum_2 != 0:
        return True
    if i == len(T):
        return False
    return zad_2(T, sum_1+dec_to_bin(T[i]), sum_2, sum_3, i+1) or zad_2(T, sum_1, sum_2+dec_to_bin(T[i]), sum_3, i+1)\
           or zad_2(T, sum_1, sum_2, sum_3+dec_to_bin(T[i]), i+1)


if __name__ == '__main__':
    #T = [2,3,5,7,11,13,17]
    T = [5, 3, 7]
    print(zad_2(T))