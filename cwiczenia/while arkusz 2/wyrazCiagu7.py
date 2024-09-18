def zad(num):
    a=3
    n=1
    while a<=num:
        if num%a==0:
            return True
        n+=1
        a=n*n+n+1
    return False

#3 7 13 21 31 43 57 

print(zad(51)) 
