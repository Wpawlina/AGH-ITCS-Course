import math

def pi(pres):
    a=math.sqrt(0.5)
    iloczyn=a
    for i in range(1,pres):
        a=math.sqrt(0.5+0.5*a)
        iloczyn=iloczyn*a
    return 2/iloczyn

print(pi(1000000000000))
