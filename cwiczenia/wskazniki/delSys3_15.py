def CzyWiecej(n):
    jedynek=0
    dwojek=0
    while n!=0:
        dig=n%3
        if dig==1:
            jedynek+=1
        if dig==2:
            dwojek+=1
        n//=3
    return jedynek>dwojek
def zad15(first):
    q=first
    p=first.next
    while p is not None:
        if CzyWiecej(p.val):
            q.next=p.next
        else:
            q=p
        p=p.next
        


