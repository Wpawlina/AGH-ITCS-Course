
def zad21(first):
    q=None
    p=first
    maxl=1
    maxq=None
    maxp=None
    curl=1
    curq=None
    cntmax=0
    while p is not None:
        if p.next is not None and p.val < p.next.val:
            curl+=1
            if curl==2:
                curq=q
            if curl > maxl:
                maxl=curl
                maxp=p.next
                maxq=curq
                cntmax=1
            if maxl==curl:
                cntmax+=1
        else:
            curl=1
            curq=None
        q=p
        p=p.next
    if maxl>=2 and cntmax==1:
        if maxq is not None:
            maxq.next=maxp.next
        else:
            first=maxp.next
    return first





