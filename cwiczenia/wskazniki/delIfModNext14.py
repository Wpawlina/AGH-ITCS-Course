def zad14(first):
    cur=first
    prev=None
    while cur is not None:
        if cur.next is not None and cur.val%cur.val.next==0:
            if prev is not None:
                prev.next=cur.next
            else:
                first=cur.next
        else:
            prev=cur
        cur=cur.next
    return first

            
