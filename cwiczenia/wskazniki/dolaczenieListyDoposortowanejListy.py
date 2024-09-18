def zad30(l1,l2):
    p1=l1
    p2=l2.next
    while p2 is not None:
        q=p1
        p=p1.next
        while p is not None and p.val < p2.val:
            q=p
            p=p.next
        if p is None:
            q.next=p2
            p2=p2.next
        elif p.val > p2.val:
            q.next=p2
            p2.next,p2=p,p2.next
        else:
            p2=p2.next
    return l1

        
        


