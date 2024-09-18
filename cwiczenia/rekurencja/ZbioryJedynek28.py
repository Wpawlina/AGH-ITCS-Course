def ileJedynek(n):
    ile=0
    while n!=0:
        ile+=n%2
        n//=2
    return ile
def zad28(T):
    n=len(T)
    def rek(i,A,B,C):
        if A==B and B==C and A!=0:
            return True
        if i==n:
            return False
        return rek(i+1,A+ileJedynek(T[i]),B,C) or rek(i+1,A,B+ileJedynek(T[i]),C) or rek(i+1,A,B,C+ileJedynek(T[i]))
    return rek(0,0,0,0)
T=[2,3,5,7,15]
print(zad28(T))

    
    
