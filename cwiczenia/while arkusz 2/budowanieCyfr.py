


def ile_jedynek_w_systemie_binarnym(num):
    cnt=0
    while num!=0:
        cnt=cnt+num%2
        num=num//2
    return cnt
def liczba_cyfr(num):
    cnt=0
    while num!=0:
        cnt+=1
        num//=10
    return cnt

def zlacz_liczby(num1,num2,maska):
    result=0
    p=0
    while num1!=0 and num2!=0:
        d=maska%2
        if d==1:
            result+=(num1%10)*(10**p)
            num1//=10
        else:
            result+=(num2%10)*(10**p)
            num2//=10
        maska//=2
        p+=1
    return result+(num1*(10**p))+(num2*(10**p))
def pierwsza(n):
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


def ileLiczbPierwszych(num1,num2):
   cnt=0
   liczba_jedynek=liczba_cyfr(num1)
   dlugosc_maski=liczba_jedynek+liczba_cyfr(num2)
   max_maska=0
   for i in range(1,liczba_jedynek+2):
       max_maska+=2**(dlugosc_maski-i)
   for m in range(1,max_maska):
       if liczba_jedynek==ile_jedynek_w_systemie_binarnym(m):
           if pierwsza(zlacz_liczby(num1,num2,m)):
               print(zlacz_liczby(num1,num2,m))
               cnt+=1
   return cnt

print(ileLiczbPierwszych(81,91))               
           

