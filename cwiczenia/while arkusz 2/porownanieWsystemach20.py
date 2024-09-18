def diffDigits(a,b,system):
    digit=[False]*system
    while a!=0:
        digit[a%system]=True
        a//=system
    while b!=0:
        if digit[b%system]==True:
            return False
        b//=system
    return True
def zad(a,b):
    i=2
    while i<=16:
        if diffDigits(a,b,i):
            return i
        i+=1
    return 'Brak takiego systemu'
print(zad(123,522))
    