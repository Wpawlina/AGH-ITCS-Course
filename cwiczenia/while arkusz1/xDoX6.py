from math import e,log

def f(x):
    return x**x-2020
def f_prim(x):
    return (x**x)*(log(x,e)+1)

def newton(x,eps=10e-6):
    while(abs(f(x))>eps):
        x=x-(f(x)/f_prim(x))
    return x,f(x)+2020
print(newton(4))