class Node:
 def __init__(self,val=None) :
    self.val=val
    self.next=None

def member(zb,el):
    while zb!=None and zb.val <el:
        zb=zb.next
    return zb!=None and zb.val==el
def memberRek(zb,el):
    if zb==None: return False
    if zb.val==el: return True
    if zb.val>el: return False
    return member(zb.next,el)
def insert(first,el):
    zb=first
    q=None
    while zb!=None and zb.val<el:
        q=zb
        zb=zb.next
    if zb!=None and zb.val==el: return
    p=Node(el)
    p.next=zb
    if q!=None:
       q.next=p
       return first
    else:
       return p
def insertRek(first,el):
    if first==None:
        p=Node(el)
        return p 
    if first.val==el:
       return first
    else:
       first.next=insertRek(first.next,el)
       return first
def deleteRek(first,el):
    if first==None:
       return None
    if first.val==el:
       return first.next
    else:
       first.next=deleteRek(first.next,el)
       return first
def delete(first,el):
   q=None
   zb=first
   while zb!=None and zb.val<el:
      q=zb
      zb=zb.next
   if zb==None or zb.val > el : return first
   if q!=None:
      q.next=zb.next
      return first
   else:
      return None
   
      

       
       
       
    
       
    



    

    



  
  