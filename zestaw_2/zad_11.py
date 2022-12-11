def if_increasing(num):
    while num > 0:
        x = num % 10
        num //= 10
        if num % 10 >= x:
            return False
    return True


if __name__ == '__main__':
    print(if_increasing(467))