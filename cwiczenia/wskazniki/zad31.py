def zad31(first):
    cur=first
    even=None
    startE=None
    odd=None
    startO=None
    cnt=0
    while cur is not None:
        if cur.val%2==0 and cur.val>0:
            if even is None:
                even=cur
                startE=even
            else:
                even.next=cur
                even=even.next
        elif cur.val%2==1 and cur.val<0:
            if odd is None:
                odd=cur
                startO=odd
            else:
                odd.next=cur
                odd=odd.next
        else:
            cnt+=1
        cur=cur.next
    if odd is not None:
        odd.next=None
    if even is not None:
        even.next=None
    return startE,startO,cnt


