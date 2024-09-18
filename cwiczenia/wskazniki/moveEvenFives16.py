def CzyParzysta(n):
    ile=0
    while n!=0:
        dig = n%8
        if dig==5:
            ile+=1
        n//=8
    return ile%2==0


def zad16(first):
    q=first
    p=first.next
    while p is not None:
        if CzyParzysta(p.val):
            if q!=first:
                q.next=p.next
                p.next=first.next
                first.next=p
                p=q.next
        else:
            q=p
            p=p.next
        

