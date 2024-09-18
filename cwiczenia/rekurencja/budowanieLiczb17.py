from math import log10
def isPrime(n):
    if n<0:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
        if n%i==0:
            return False
        i+=4
    return True
def ileCyfr(num):
    return int(log10(num))+1
def zad17(num1,num2):
    n=ileCyfr(num1)
    m=ileCyfr(num2)
    ile=0
    def rek(i,a,b,num,num1,num2):
        nonlocal ile
        if i==n+m:
            if isPrime(num):
                print(num)
                ile+=1
            return
        if a<n:
            dig=num1//(10**(ileCyfr(num1)-1))
            rek(i+1,a+1,b,num*10+dig, num1%(10**(ileCyfr(num1)-1)),num2)
        if b<m:
            dig=num2//(10**(ileCyfr(num2)-1))
            rek(i+1,a,b+1,num*10+dig,num1,num2%(10**(ileCyfr(num2)-1)))
    rek(0,0,0,0,num1,num2)
    return ile
print(zad17(81,91)) 

  
