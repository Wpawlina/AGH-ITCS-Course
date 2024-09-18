
class Node:
    def __init__(self,value):
        self.val=value
        self.next=None


def zad5(first):
    firstL=[None for _ in range(10)]
    curL=[None for _ in range(10)]
    cur=first
    while cur is not None:
        index = cur.val% 10
        

        if curL[index] is not None:
            curL[index].next = cur
            curL[index] = curL[index].next
        else:
            curL[index] = cur
            firstL[index] = curL[index]

        cur = cur.next
    result_head = None
    result_tail = None

    for i in range(10):
        if firstL[i] is not None:
            if result_head is None:
                result_head = firstL[i]
                result_tail = curL[i]
            else:
                result_tail.next = firstL[i]
                result_tail = curL[i]
    return result_head
    




def initSparseTab(ile,default):
    if ile>0:
        p=Node(default)   
        first=p
        for i in range(1,ile):
            new=Node(default)
            p.next=new
            p=p.next
        return first
    return None
def printN(first,n):
    wsk=first
    i=0
    while wsk!=None and i<n:
        wsk=wsk.next
        i+=1
    if wsk==None:
        return None
    print(wsk.val,i) 
def setN(first,n,value):
    wsk=first
    i=0
    while wsk!=None and i<n:
        wsk=wsk.next
        i+=1
    if wsk==None:
        return None
    wsk.val=value
first=initSparseTab(20,10)

for i in range(20):
   setN(first,i,i)

for i in range(20):
    printN(first,i)


print('###############')

first=zad5(first)

for i in range(20):
    printN(first,i)





