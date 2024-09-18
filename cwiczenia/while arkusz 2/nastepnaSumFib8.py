def zad(num):
    if num<4:
        return 4
    else:
        return num+1 if generujFib(num)!=num+1 else num +2 
    
      


def generujFib(num):
    a=0
    b=1
    while b<=num:
        a,b=b,a+b
    return b

print(zad(514228))
    
