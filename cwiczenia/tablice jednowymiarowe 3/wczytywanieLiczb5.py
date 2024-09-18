def zad5(n):
    t=[0]*n
    while True:
        x=int(input('Podaj kolejna liczbę: '))
        if x==0:
            break
        for i in range(n):
            if x > t[i]:
                x,t[i]=t[i],x
    return t[n-1]
    
print(zad5(5))
    
