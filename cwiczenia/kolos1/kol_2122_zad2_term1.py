def czy4zgodne(num1,num2):
    digits=[0]*4
    while num1!=0:
        d=num1%4
        digits[d]=1
        num1//=4
    while num2!=0:
        d=num2%4
        if digits[d]==0:
            return False
        else:
            digits[d]=2
    for i in range(4):
        if digits[i]==1:
            return False
    return True
def zad2(t):
    n=len(t)
    maxl=0
    curl=1
    for i in range(n-1):
        if czy4zgodne(t[i],t[i+1]):
            curl+=1
        else:
            maxl=max(maxl,curl)
            curl=1
    return maxl if maxl > 1 else 0
    
    

    
    