def waga(num):
    cnt=0
    i=2
    while num!=1:
        if num %i==0:
            cnt+=1
            while num%i==0:
                num//10
        i+=1
    return cnt

def zad2(T):
    n=len(T)
    # zwraca informacje czy da sie utowrzyc takie zbiory
    #i numer elementu w jakim teraz jestesmy
    #a,b,c wagi zbiorów
    def rek(i,a,b,c):
        if i==n:
            return a==b and b==c
        return rek(i+1,a+waga(T[i]),b,c) or rek(i+1,a,b+waga(T[i]),c) or rek(i+1,a,b,c+waga(T[i]))
    return rek(0,0,0,0)

    
