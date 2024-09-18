
        
def zad28(l1,l2):
    prev=None
    cur=l2
    cnt=0
    while l2 is not None:
        q=None
        p=l1
        flag=False
        while p is not None and p.val<l2.val:
            q=p
            p=p.next    
        if p is not None and p.val == l2.val:
            flag=True
            cnt+=2
            if q is None:
                l1=p.next
            else:
                q.next=p.next
        if flag:
            if prev is None:
                l2=cur.next
            else:
                prev.next=cur.next
        else:
            prev=cur
        cur=cur.next
    return cnt
        

        
            
