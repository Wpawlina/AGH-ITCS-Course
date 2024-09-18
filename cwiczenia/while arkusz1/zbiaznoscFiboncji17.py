def zbiegFib(a,b,eps=10e-3):
    fibRatioPrev=b/a
    a,b=b,a+b
    fibRatioCur=b/a
    while abs(fibRatioPrev-fibRatioCur)>eps:
        fibRatioPrev=fibRatioCur
        a,b=b,a+b
        fibRatioCur=b/a
    return fibRatioCur
print(zbiegFib(1,1))