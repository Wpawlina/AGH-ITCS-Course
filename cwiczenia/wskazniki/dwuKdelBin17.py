def OddNumOnesBin(n):
    cnt=0
    while n!=0:
        dig = n%2
        cnt+=dig
        n//=2
    return cnt%2==1
def zad17(first):
    p=first
    q=None
    if p is not None:
        n=p.next
    while p is not None:
        if OddNumOnesBin(p.val):
            if q is not None:
                q.next=p.next
            else:
                first=p.next
            if n is not None:
                n.prev=q
        else:
            q=p
        if n is not None:
            n=n.next
        p=p.next
    return first
