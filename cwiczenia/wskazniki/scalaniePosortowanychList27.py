def scal(firstL1,firstL2):
    if firstL1==None:
        return firstL2
    if firstL2==None:
        return firstL1
    firstL3=None
    l3=None
    l1=firstL1
    l2=firstL2
    while l1!=None and l2!=None:
        if l1.val<l2.val:
            if l3!=None:
                l3.next=l1
                l3=l3.next
            else:
                 firstL3=l1
            l1=l1.next
        else:
            if l3!=None:
                l3.next=l2
                l3=l3.next
            else:
                firstL3=l2
            
            l2=l2.next
    if l1!=None:
        l3.next=l1
    if l2!=None:
        l3.next=l2
    return firstL3
def scalRek(firstL1,firstL2):
    if firstL1==None:
        return firstL2
    if firstL2==None:
        return firstL1
    if firstL1.val<firstL2.val:
           firstL1.next=scalRek(firstL1.next,firstL2)
           return firstL1
    else:
        firstL2.next=scalRek(firstL1,firstL2.next)
        return firstL2
    
    
    



    
    





