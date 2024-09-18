def CzyCykliczna(first):
    slow=first
    fast=first
    while fast!=None:
        slow=slow.next
        fast=fast.next
        if fast==None:
            return False
        fast.next
        if fast==slow:
            return True   
    return False

        
