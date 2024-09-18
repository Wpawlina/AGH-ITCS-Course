def zad(year):
    a=1
    b=1
    mins=year+1
    ap=0
    bp=0
    for a in range(1,year):
        for b in range(a,year):
            if sprawdzCiag(a,b,year):
                if mins>a+b:
                    mins=a+b
                    ap=a
                    bp=b
    return ap,bp



    

def sprawdzCiag(a,b,year):
    while b<year:
        a,b=b,a+b
    if b==year:
        return True
    else:
        return False


print(zad(2023))