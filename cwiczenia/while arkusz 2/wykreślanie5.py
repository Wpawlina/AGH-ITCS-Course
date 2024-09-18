def zad(num):
    num=str(num)
    n=len(num)
    ile=0
    for i in range(n):
        for j in range(i+1,n):
            test=num[:i]+num[i+1:j]+num[j+1:]
            test=int(test)
            if test%7==0:
                ile+=1
    return ile

print(zad(2315))
