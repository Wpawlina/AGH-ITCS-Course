import random

def tablica(n):
    list=[0]*n
    for i in range(0,n):
        list[i]=random.randint(1,1000)
        if nieparzysta(list[i]):
            return True
    return False



def nieparzysta(num):
    while num!=0:
        dig=num%10
        n//=10
        if dig%2==0:
            return False
    return True