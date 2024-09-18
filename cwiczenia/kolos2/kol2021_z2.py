def czy_samogloska(char):
    if char in ('a','o','u','i','e','y'):
        return True
    return False
def cutting(s):
    ile=0
    n=len(s)
    def rek(i,prev):
        nonlocal ile
        if i==n:
            ile+=prev
            return
        if czy_samogloska(s[i]):
            if prev==1:
                rek(i+1,1)
            else:
                rek(i+1,1)
        else:
            if prev==1:
                rek(i+1,1)
                rek(i+1,0)
            else:
                rek(i+1,0)
    rek(0,0)
    return ile
print(cutting('ocena'))
            
    