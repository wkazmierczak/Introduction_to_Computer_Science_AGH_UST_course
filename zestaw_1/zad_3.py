sum = int(input("Enter sum: "))
i = 0
current_sum = 1
second_sum = 0
list = [1]
current_diff = 0
fib = 0
num1 = 1
num2 = 0


while True:
    fib = num1 + num2
    num2 = num1
    num1 = fib
    current_sum += fib
    list.append(num1)
    if current_sum > sum:
        break
    elif current_sum == sum:
        print("done")
        print(list)
        break


for i in range(len(list)):
    second_sum += list[(-1-i)]
    if second_sum == sum:
        print("done")
        print(list[(-1-i):])
        quit()
print("not done")