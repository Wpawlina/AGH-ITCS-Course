def checkSeq(A,B):
    n=len(A)
    w=B[0]/A[0]
    for i in range(1,n):
        if (B[i]/A[i])!=w:
            return False
    return True

def zad1(t):
    n=len(t)
    l=n//2
    while l >=3:
        i=0
        while i+2*l <=n:
            if checkSeq(t[i:i+l],t[i+l:i+2*l]):
               return i,i+l-1
            i+=1
        l-=1
    return None
t=[2,5,7,3,2,3,5,7,6,9,15,21]
print(zad1(t))
        

        


