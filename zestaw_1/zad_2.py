fib = 0
num1 = 1000
num2 = 1022

print(num1)


while num1+num2 <= 1000000:
    fib = num1 + num2
    num2 = num1
    num1 = fib
    print(num1)