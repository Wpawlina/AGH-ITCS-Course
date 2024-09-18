def maxFragment(t):
    n=len(t)
    maxl=0
    i=0
    while i< n-maxl:
        iloczyn=t[i]
        if jedenCzynnik(iloczyn):
            l=1
            for j in range(i+1,n):
                iloczyn*=t[j]
                if not jedenCzynnik(iloczyn):
                    break
                l+=1
            maxl=max(maxl,l)
        i+=1
    return maxl


def jedenCzynnik(num):
    i=2
    while i*i<=num and num!=1:
        numberI=0
        while num%i==0:
            numberI+=1
            num//=i
            if numberI ==2:
                return False
        i+=1
    return True

t=[2,2,2,3,5,7,11,13,17,19,5,4,3,3,5,11,13]
print(maxFragment(t))
