def pole(p,k,pre=10):
    pole=0
    d=(k-p)/pre
    while p<k:
        x=(p+p+d)/2
        pole+=d*f(x)
        print(p)
        p+=d
        
    return pole
def f(x):
    return 1/x

print(pole(1,11,10))