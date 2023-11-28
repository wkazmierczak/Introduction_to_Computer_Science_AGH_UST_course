# Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.

from random import randint

def zad_23(T, R, curr_R=0, taken=3, i=0):
    if R == curr_R and taken == 0:
        return True
    if  i == len(T) or taken < 0:
        return False
    
    return zad_23(T, R, curr_R+T[i],taken-1, i+1) or zad_23(T, R, (curr_R*T[i])/(curr_R+T[i]), taken-1, i+1) or zad_23(T, R, curr_R , taken, i+1)


if __name__ == '__main__':
    T = [2, 7, 2]
    print(zad_23(T, 8))