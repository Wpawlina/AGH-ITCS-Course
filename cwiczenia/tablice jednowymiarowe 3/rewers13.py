
def rewers(t):
    n=len(t)
    rev=t[::-1]
    maxl=1
    left=0
    right=0
    while right < n:
        if podciag(t[left:right+1],rev):
            right+=1
        else:
            left+=1
        if podciag(t[left:right],rev):
            maxl=max(maxl,right-left)
    return maxl



def  podciag(a,b):
    for i in range(len(b)-len(a)+1):
        if b[i:i+len(a)]==a:
            return True
    return False


    
    











t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] 

print(rewers(t))