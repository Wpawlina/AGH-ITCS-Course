
def A(n):
    suma=1
    for i in range(2,n):
        if n%i==0:
            suma+=i
    return suma
def B(n):
    if n==1:
        return 1
    a=1
    b=1
    while b<=n:
        a,b=b,a+b
    return b
def C(n):
    rewers=0
    x=n
    while x!=0:
        dig=x%10
        rewers=rewers*10+dig
        x//=10
    return n+rewers
def cycle(x,n):
    initX=x
    value=0
    def rek(x,i,s):
        nonlocal value
        if i > 1 and x==initX:
            print(s+str(x))
            value=i
        if i==n:
            return
        rek(A(x),i+1,s+str(x)+'A')
        if value>1:
            return
        rek(B(x),i+1,s+str(x)+'B')
        if value>1:
            return
        rek(C(x),i+1,s+str(x)+'C')

        

    rek(x,0,'')
    return value
print(A(44))
print(cycle(29,6))

            
