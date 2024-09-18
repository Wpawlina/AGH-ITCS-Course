def dwaCzynniki(n):
    fact=0
    i=2
    while n!=1:
        if n%i==0:
            fact+=1
            if fact > 2:
                return False
            while n%i==0:
                n//=i
        i+=1
    return True if fact==2 else False







def zad2(t):
    n=len(t)
    l=2
    while l <n:
        i=0
        while i+l<=n:
            j=0
            while j+l<=n:
                iloczyn=t[i][j]*t[i][j+l-1]*t[i+l-1][j]*t[i+l-1][j+l-1]
                if dwaCzynniki(iloczyn):
                    return l
                j+=1
            i+=1
        l+=1
    return 0


t=[
    [30,30,30,30,30],
    [30,2,30,3,30],
    [30,30,2,30,3],
    [30,5,30,3,30],
    [30,30,2,30,2]
]

print(zad2(t))