given_num = int(input("Enter num: "))
sum = 0
n = 1
flag = 0

while sum < given_num:
    n += 2
    sum += n
    flag += 1
print(flag)
