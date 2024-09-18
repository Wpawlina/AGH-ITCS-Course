a=0
b=2
x=int(input('podaj pierwszy wyraz ciagu a '))
if x==a:
    print(b)
    a,b,ap=1,b+2*a,a
    x=int(input('podaj kolejny wyraz ciagu a '))
    while x==a:
        print(b)
        a,b,ap=a-b*ap,b+2*a,a
        x=int(input('podaj kolejny wyraz ciagu a '))

