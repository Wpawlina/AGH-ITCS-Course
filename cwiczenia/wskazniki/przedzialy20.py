


def zad20(first):
    cur=first
    while cur is not None:
        p=cur.next
        q=cur
        while p is not None:
            if p.start <= cur.end and p.end >= cur.start:
                cur.start=min(cur.start,p.start)
                cur.end=max(cur.end,p.end)
                q.next=p.next
                p=cur.next
                q=cur
           
            else:
                q=p
                p=p.next
        cur=cur.next

        
