def wyszukaj(root,n):
    if root is None:
        return None
    if root.val==n:
        return root
    if n>root.val:
        return wyszukaj(root.right,n)
    if n<root.val:
        return wyszukaj(root.left,n)