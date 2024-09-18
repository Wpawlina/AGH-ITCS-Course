def zad24(first):
    slow=first
    fast=first
    while fast is not None:
        slow=slow.next
        fast=fast.next
        if fast is None:
            return 0
        fast=fast.next
        if fast==slow:
            cnt=0
            slow2=first
            while slow!=slow2:
                slow=slow.next
                slow2=slow2.next
                cnt+=1
            return cnt
    #jesli lista nie ma cyklu wtedy zwracamy dlugosc tej listy 
    cnt=0
    slow=first
    while slow is not None:
        cnt+=1
        slow=slow.next
    return cnt 
    