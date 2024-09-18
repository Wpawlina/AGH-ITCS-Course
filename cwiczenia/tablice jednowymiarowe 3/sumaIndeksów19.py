def zad19(t):
    n=len(t)
    maxc=0
    for i in range(n-1):
        sum=t[i]
        cnt=1
        sum_ind=i
        for j in range(i,n-1):
            if not t[j]<t[j+1]:
                break
            else:
                cnt+=1
                sum_ind+=j+1
                sum+=t[j+1]
                if sum==sum_ind:
                    maxc=max(maxc,cnt)
    return maxc






t=[1,2,1,3,5,6,7,5,8,9,1,7,4]
print(zad19(t))