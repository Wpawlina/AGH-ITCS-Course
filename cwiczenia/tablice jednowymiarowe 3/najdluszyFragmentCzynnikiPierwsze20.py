
def maxFragment(t):
    n=len(t)
    primeFactor=[0]*1000
    maxl=0
    left,right=0,0
    while right<n:
        if max(primeFactor)<=1:
            num=t[right]
            d=2
            while num!=1:
                if num%d==0:
                    primeFactor[d]+=1
                    num//=d
                else:
                    d+=1
        
            right+=1
        else:
            num=t[left]
            d=2
            while num!=1:
                if num%d==0:
                    primeFactor[d]-=1
                    num//=d
                else:
                    d+=1
            left+=1
        if max(primeFactor)<=1:
            maxl=max(maxl,right-left)
    return maxl


t=[2,3,5,7,5,4,3,3,5,11,13] 
print(maxFragment(t))       


'''
a1 2
a2 1,5,7,8,9,14,18
a3 2,15




'''
                
                