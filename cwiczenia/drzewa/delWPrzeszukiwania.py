def findMin(node):
    if node.left is None:
        return node
    return node.left



def delete(node):
    if node.left==None and node.right==None:
        if node.parent.left==node:
            node.parent.left=None
        elif node.parent.right==node:
            node.parent.right=None
    elif node.left is not None and node.right is None:
        if node.parent.left==node:
            node.parent.left=node.left
        elif node.parent.right==node:
            node.parent.right=node.left
    elif node.left is None and node.right is not None:
        if node.parent.left==node:
            node.parent.left=node.right
        elif node.parent.right==node:
            node.parent.right=node.right
    elif node.left is not None and node.right is not None:





