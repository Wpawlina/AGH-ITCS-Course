def sumaKluczy(root):
    if root is None:
        return 0
    return root.val + sumaKluczy(root.left) + sumaKluczy(root.right)
def sumaPoziomow(root,n,i=1):
    if root is None:
        return 0
    if i==n:
        return root.val
    return sumaPoziomow(root.left,n,i+1) + sumaPoziomow(root.right,n,i+1)
    



