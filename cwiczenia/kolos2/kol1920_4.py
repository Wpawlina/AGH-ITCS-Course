from math import log10

def ileCyfr(n):
    return int(log10(n))+1

def isPrime(n):
    if n<2:
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
   
def zad4(n):
    value=False
    def divide(n,prev,counter):
        nonlocal value
        if n==0:
            
            if isPrime(prev) and isPrime(counter):
                value=True
            return
        dig=n%10
        if counter==0:
            divide(n//10,dig,counter+1)
        else:
            if not isPrime(prev):
                divide(n//10,prev+dig*10**ileCyfr(prev),counter)
            else:
                divide(n//10,dig,counter+1)
                if value==True:
                    return 
                divide(n//10,prev+dig*10**ileCyfr(prev),counter)
    divide(n,None,0)
    return value

print(zad4())

        
                
            
    
    
        

    
    
    
    


        