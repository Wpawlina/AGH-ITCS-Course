def zad(n):
    a=1
    b=1
    while b<=n:
        if n%b==0:
            if czyFib(n//b):
                return True
        a,b=b,a+b
    return False
def czyFib(n):
    a=1
    b=1
    while b<n:
        a,b=b,a+b
    if b==n:
        return True
    else:
        return False


print(zad(20))