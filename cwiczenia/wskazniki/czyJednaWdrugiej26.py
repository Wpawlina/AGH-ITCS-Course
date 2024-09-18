def zad26(l1,l2):
    if l2 is None:
        return False
    while l1 is not None:
        if l1.val == l2.val:
            i=l2
            j=l1
            while j is not None and i is not None and i.val == j.val:
                i = i.next
                j = j.next     
            if i is None:
                return True 
        l1=l1.next
    return False



