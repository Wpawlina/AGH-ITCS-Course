import math
def newton_3(V,epsilon):
    a=1
    b=1
    c=V/(a+b)
    while  math.fabs(a-c) > epsilon:
        a=(a+b+c)/3
        b=(a+b+c)/3
        c=V/(a*b)
    return (a+b+c)/3
print(newton_3(8,0.0000001))


