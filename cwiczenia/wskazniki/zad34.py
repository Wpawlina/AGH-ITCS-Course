def zad34(first,k):
    prev=first
    if first is None:
        return None
    cur=first.next
    check=first.next
    wynik=False
    flag=False
    while cur!=check or not flag:
        cnt=1
        test=cur.next
        while test!=check:
            if test.val==cur.val:
                cnt+=1
            test=test.next
        if cnt==k:
            wynik=True
            prevt=cur
            test=cur.next
            while test!=check:
                if test.val==cur.val:
                    prevt.next=test.next
                else:
                    prevt=test
                test=test.next
            prev.next=cur.next
        else:
            prev=cur
        cur=cur.next
        flag=True
        
            


