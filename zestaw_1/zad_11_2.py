for y in range (1,1000001):
    k = y-1
    suma1  = 0
    while k>0 :
        if y%k==0:
            suma1+=k
        k-=1
    for x in range (y,1000000):
        p = x - 1
        suma2 = 0
        while p > 0:
            if x % p == 0:
                suma2 += p
            p -= 1
        if suma1==x and suma2==y and x!=y:
            print("Znalazłem parę liczb zaprzyjaźnionych:",x,y)
