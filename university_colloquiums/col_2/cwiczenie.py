

def zliczanie(num):
    if num == 0:
        return 0
    
    return 1 + zliczanie(num//2)

print(zliczanie(458787))