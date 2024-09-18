def zad23(first):
    fast=first
    slow=first
    cnt=0
    while fast is not None:
        slow=slow.next
        fast=fast.next
        if fast is None:
            return 0
        fast=fast.next
        if fast==slow:
            p=fast.next
            cnt=1
            while p!=fast:
                cnt+=1
                p=p.next
            return cnt
    return 0


            
                

        